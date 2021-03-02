"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>

Usage:
    python -m src.resource.script.scaffold.scaffold
    # Print config
    python -m src.resource.script.scaffold.scaffold print-config config.yaml
    # Generate code
    python -m src.resource.script.scaffold.scaffold generate config.yaml
"""

import json
import os
import sys
import traceback
from pathlib import Path

import click
import emoji
import yaml
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from src.resource.common.Util import Util


# region Global config & settings
class FrontTextTerminalColor:
    BLUE = "\x1b[34m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    RED = "\x1b[31m"
    RESET = "\x1b[0m"
    BLACK = "\x1B[30m"
    CYAN = "\x1b[36m"
    BOLD = "\x1B[1m"
    MAGENTA = "\x1b[35m"
    UNDERLINE_ON = "\x1b[4m"
    UNDERLINE_OFF = "\x1b[24m"


class BackgroundTextTerminalColor:
    BLUE = "\x1B[44m"
    GREEN = "\x1B[42m"
    YELLOW = "\x1B[43m"
    RED = "\x1B[41m"
    RESET = "\x1b[0m"
    CYAN = "\x1b[46m"
    BLACK = "\x1B[40m"
    MAGENTA = "\x1b[45m"
    UNDERLINE_ON = "\x1b[4m"
    UNDERLINE_OFF = "\x1b[24m"


class Config:
    configData = None
    projectPath = None
    templatePath = None
    configFilePath = None

    @staticmethod
    def __repr__():
        return f'{FrontTextTerminalColor.GREEN}projectPath:{FrontTextTerminalColor.RESET} {Config.projectPath}\n' \
               f'{FrontTextTerminalColor.GREEN}templatePath:{FrontTextTerminalColor.RESET} {Config.templatePath}\n' \
               f'{FrontTextTerminalColor.GREEN}configFilePath:{FrontTextTerminalColor.RESET} {Config.configFilePath}\n' \
               f'{FrontTextTerminalColor.GREEN}configData:{FrontTextTerminalColor.RESET} {json.dumps(Config.configData, indent=2)}\n'


# endregion

# region Cli commands
@click.group()
def cli():
    pass


@cli.command(help='Generate code files based on a config file')
@click.argument('config_file')
def generate(config_file):
    # Init the config data
    initConfigData(config_file)
    # Generate routes
    generateRoute()
    # Generate model response
    generateRouterModelResponse()
    # Generate grpc api client
    generateGrpcApiClient()
    # Generate protocol buffer files
    generateProtoBuffer()
    # Generate command constants
    generateCommandConstant()


@cli.command(help='Print config data')
@click.argument('config_file')
def print_config(config_file):
    initConfigData(config_file)
    print(Config.__repr__())


# endregion

# Read the config data and save it into Config class
def initConfigData(configFile):
    configData = readConfig(configFile)
    Config.configData = configData


# Initialize the global configuration, provide full paths to the script
def initGlobalConfig():
    Config.projectPath = os.path.abspath(f'{os.path.dirname(__file__)}/../../../..')
    Config.templatePath = f'{Config.projectPath}/src/resource/script/scaffold/template'
    Config.configFilePath = f'{Config.projectPath}/src/resource/script/scaffold'


# Read config yaml file
def readConfig(configFile) -> dict:
    try:
        with open(f'{Config.configFilePath}/{configFile}', 'r') as file:
            return yaml.load(file, Loader=yaml.FullLoader)
    except:
        print(traceback.format_exc())
        print('Could not read config file')
        sys.exit(1)


# Generate protocol buffer files
def generateProtoBuffer():
    _print(modelName='', message=':gear: Generating protocol buffer files')
    protoPath = Config.configData['global']['path']['proto_buffer']
    protoFullPath = f'{Config.projectPath}/{protoPath}'
    _createDir(path=protoFullPath)
    for modelConfig in Config.configData['domain_model']:
        isGenerated = False
        model = modelConfig['model']
        doNotSkip = True if ('skip' in model and 'proto' not in model['skip'] and 'all' not in model['skip']) or (
                'skip' not in model) else False
        if doNotSkip:
            modelProtoName = f'{protoFullPath}/{model["microservice"]}/{model["name"]}'
            modelTemplate = jinjaEnv.get_template(f'proto/model.jinja2')
            modelAppTemplate = jinjaEnv.get_template(f'proto/segment.jinja2')
            renderedTemplate = modelTemplate.render(model=model)
            skipGeneratingFile = False
            if ('file_overwrite' not in model) or ('file_overwrite' in model and model['file_overwrite'] is False):
                if _isManuallyModified(fileFullPath=f'{modelProtoName}.proto', templateString=renderedTemplate):
                    _print(modelName='',
                           message=f':locked: the current file {modelProtoName}.proto is different from the template, enable file_overwrite to overwrite it',
                           innerDepth=1, error=True)
                    skipGeneratingFile = True
            if not skipGeneratingFile:
                isGenerated = True
                with open(f'{modelProtoName}.proto', 'w+') as file:
                    file.write(renderedTemplate)
                    file.write('\n')
                _print(modelName=f'{model["name"]}', message=f'{modelProtoName}.proto', innerDepth=1)
            renderedTemplate = modelAppTemplate.render(model=model, segment=Config.configData['segment'])
            skipGeneratingFile = False
            if ('file_overwrite' not in model) or ('file_overwrite' in model and model['file_overwrite'] is False):
                if _isManuallyModified(fileFullPath=f'{modelProtoName}_app_service.proto',
                                       templateString=renderedTemplate):
                    _print(modelName='',
                           message=f':locked: the current file {modelProtoName}_app_service.proto is different from the template, enable file_overwrite to overwrite it',
                           innerDepth=1, error=True)
                    skipGeneratingFile = True
            if not skipGeneratingFile:
                with open(f'{modelProtoName}_app_service.proto', 'w+') as file:
                    file.write(renderedTemplate)
                    file.write('\n')
                _print(modelName=f'{model["name"]}', message=f'{modelProtoName}_app_service.proto', innerDepth=1)
        if isGenerated:
            _print(modelName=model["name"], message='done generating code for #modelName :thumbs_up:', innerDepth=1)
        else:
            _print(modelName=model["name"], message='nothing is generated for #modelName :frog:', innerDepth=1)


# Generate protocol buffer files
def generateCommandConstant():
    messagePath = Config.configData['global']['path']['messaging']
    messageFullPath = f'{Config.projectPath}/{messagePath}'
    _createDir(path=messageFullPath)
    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        doNotSkip = True if ('skip' in model and 'command_constant' not in model['skip'] and 'all' not in model[
            'skip']) or ('skip' not in model) else False
        if doNotSkip:
            _addTemplateBeforeSignatureEnd(fullFilePath=f'{messageFullPath}/common/model/CommandConstant',
                                           template=jinjaEnv.get_template(f'messaging/command_constant.jinja2'),
                                           model=model,
                                           signatureStart='# region Command constants',
                                           signatureEnd='# endregion'
                                           )


# Generate routes for the models
def generateRoute():
    _print(modelName='', message=':gear: Generating routes')
    routerPath = Config.configData['global']['path']['router']
    routerFullPath = f'{Config.projectPath}/{routerPath}'
    _createDir(path=routerFullPath)
    for modelConfig in Config.configData['domain_model']:
        isGenerated = False
        model = modelConfig['model']
        _createDir(f'{routerFullPath}/{model["path"]}')
        doNotSkip = True if ('skip' in model and 'router' not in model['skip'] and 'all' not in model['skip']) or (
                'skip' not in model) else False
        if doNotSkip:
            modelName = f'{routerFullPath}/{model["path"]}/{model["name"]}'
            testTemplate = jinjaEnv.get_template(f'router/model.jinja2')
            renderedTemplate = testTemplate.render(model=model)
            if ('file_overwrite' not in model) or ('file_overwrite' in model and model['file_overwrite'] is False):
                if _isManuallyModified(fileFullPath=f'{modelName}.py', templateString=renderedTemplate):
                    _print(modelName='',
                           message=f':locked: the current file {modelName}.py is different from the template, enable file_overwrite to overwrite it',
                           innerDepth=1, error=True)
                    continue
            isGenerated = True
            with open(f'{modelName}.py', 'w+') as file:
                file.write(renderedTemplate)
                file.write('\n')
            _print(modelName=f'{model["name"]}', message=f'generating {modelName} for #modelName', innerDepth=1)
        if isGenerated:
            _print(modelName='', message='done :thumbs_up:', innerDepth=1)
        else:
            _print(modelName=model["name"], message='nothing is generated for #modelName :frog:', innerDepth=1)


# Generate api response models
def generateRouterModelResponse():
    _print(modelName='', message=':gear: Generating router model responses')
    modelResponsePath = Config.configData['global']['path']['router_model_response']
    modelResponseFullPath = f'{Config.projectPath}/{modelResponsePath}'
    _createDir(path=modelResponseFullPath)
    for modelConfig in Config.configData['domain_model']:
        isGenerated = False
        model = modelConfig['model']
        _createDir(f'{modelResponseFullPath}/{model["path"]}')
        doNotSkip = True if ('skip' in model and 'model_response' not in model['skip'] and 'all' not in model[
            'skip']) or (
                                    'skip' not in model) else False
        if doNotSkip:
            _print(modelName=f'{model["name"]}', message=f'generating files for #modelName', innerDepth=1)
            modelTestName = f'{modelResponseFullPath}/{model["path"]}/{Util.snakeCaseToUpperCameCaseString(model["name"])}'
            template = jinjaEnv.get_template(f'router/model_response/model.jinja2')
            renderedTemplate = template.render(model=model)
            skipGeneratingFile = False
            if ('file_overwrite' not in model) or ('file_overwrite' in model and model['file_overwrite'] is False):
                if _isManuallyModified(fileFullPath=f'{modelTestName}.py', templateString=renderedTemplate):
                    _print(modelName='',
                           message=f':locked: the current file {modelTestName}.py is different from the template, enable file_overwrite to overwrite it',
                           innerDepth=2, error=True)
                    skipGeneratingFile = True
            if not skipGeneratingFile:
                isGenerated = True
                with open(f'{modelTestName}.py', 'w+') as file:
                    file.write(renderedTemplate)
                    file.write('\n')
                _print(modelName=f'{model["name"]}', message=f'{modelTestName}.py for #modelName', innerDepth=2)

            template = jinjaEnv.get_template(f'router/model_response/models.jinja2')
            renderedTemplate = template.render(model=model)
            skipGeneratingFile = False
            if ('file_overwrite' not in model) or ('file_overwrite' in model and model['file_overwrite'] is False):
                if _isManuallyModified(fileFullPath=f'{modelTestName}s.py', templateString=renderedTemplate):
                    _print(modelName='',
                           message=f':locked: the current file {modelTestName}s.py is different from the template, enable file_overwrite to overwrite it',
                           innerDepth=2, error=True)
                    skipGeneratingFile = True
            if not skipGeneratingFile:
                isGenerated = True
                with open(f'{modelTestName}s.py', 'w+') as file:
                    file.write(renderedTemplate)
                    file.write('\n')
                _print(modelName=f'{model["name"]}', message=f'{modelTestName}s.py for #modelName', innerDepth=2)

        if isGenerated:
            _print(modelName=model["name"], message='done generating code for #modelName :thumbs_up:', innerDepth=1)
        else:
            _print(modelName=model["name"], message='nothing is generated for #modelName :frog:', innerDepth=1)


# Generate grpc client files
def generateGrpcApiClient():
    _print(modelName='', message=':gear: Generating grpc api clients')
    grpcClientPath = Config.configData['global']['path']['grpc_api_client']
    grpcClientFullPath = f'{Config.projectPath}/{grpcClientPath}'
    _createDir(path=grpcClientFullPath)
    for modelConfig in Config.configData['domain_model']:
        isGenerated = False
        model = modelConfig['model']
        _createDir(f'{grpcClientFullPath}/{model["path"]}')
        doNotSkip = True if ('skip' in model and 'grpc_client' not in model['skip'] and 'all' not in model['skip']) or (
                'skip' not in model) else False
        if doNotSkip:
            fullPathModelName = f'{grpcClientFullPath}/{model["path"]}/{Util.snakeCaseToUpperCameCaseString(model["name"])}'
            template = jinjaEnv.get_template(f'grpc/segment.jinja2')
            renderedTemplate = template.render(model=model, segment=Config.configData['segment'])
            if ('file_overwrite' not in model) or ('file_overwrite' in model and model['file_overwrite'] is False):
                if _isManuallyModified(fileFullPath=f'{fullPathModelName}Client.py', templateString=renderedTemplate):
                    _print(modelName='',
                           message=f':locked: the current file {fullPathModelName}Client.py is different from the template, enable file_overwrite to overwrite it',
                           innerDepth=1, error=True)
                    continue

            isGenerated = True
            _print(modelName=f'{model["name"]}', message=f'{fullPathModelName}Client.py for #modelName', innerDepth=1)
            with open(f'{fullPathModelName}Client.py', 'w+') as file:
                file.write(renderedTemplate)
                file.write('\n')
        if isGenerated:
            _print(modelName=model["name"], message='done generating code for #modelName :thumbs_up:', innerDepth=1)
        else:
            _print(modelName=model["name"], message='nothing is generated for #modelName :frog:', innerDepth=1)


def _isManuallyModified(fileFullPath, templateString) -> bool:
    data = None
    if os.path.exists(fileFullPath):
        with open(fileFullPath, 'r') as file:
            data = file.read()
    return data is not None and data.strip() != templateString.strip()


def _addTemplateBeforeSignatureEnd(fullFilePath, template, model, signatureStart, signatureEnd):
    tabSize = Config.configData['global']['setting']['tab_size']
    renderedTemplate = template.render(model=model)
    spaces = ' ' * tabSize
    spacedRenderedTemplate = renderedTemplate.replace('\t', spaces)
    fileLines = []
    currentContent = ''
    with open(f'{fullFilePath}.py', 'r+') as file:
        fileLines = file.readlines()
        file.seek(0)
        currentContent = file.read()
    with open(f'{fullFilePath}.py', 'w+') as file:
        if currentContent.find(spacedRenderedTemplate) == -1:
            for signatureStartIndex in range(0, len(fileLines)):
                if fileLines[signatureStartIndex].find(signatureStart) != -1:
                    for signatureEndIndex in range(signatureStartIndex + 1, len(fileLines)):
                        if fileLines[signatureEndIndex].find(signatureEnd) != -1:
                            fileLines.insert(signatureEndIndex - 1, f'{renderedTemplate}\n')
                            break
                    break
        file.writelines(fileLines)


def _print(modelName: str = None, message: str = None, innerDepth: int = 0, error: bool = False):
    colorIndex = {0: FrontTextTerminalColor.MAGENTA, 1: FrontTextTerminalColor.CYAN, 2: FrontTextTerminalColor.BLUE,
                  3: FrontTextTerminalColor.RED}
    modelString = f'{FrontTextTerminalColor.GREEN}{FrontTextTerminalColor.BOLD}{modelName}{FrontTextTerminalColor.RESET}'
    messageString = message.replace('#modelName', modelString)
    selectedIndex = innerDepth
    if error:
        selectedIndex = 3
    if innerDepth > 0:
        messageString = f'{FrontTextTerminalColor.RESET}{colorIndex[selectedIndex]}{messageString}{FrontTextTerminalColor.RESET}'
        tabs = '\t' * innerDepth
        print(emoji.emojize(f'{tabs}---> {messageString}'))
    else:
        print(emoji.emojize(
            f'{FrontTextTerminalColor.RESET}{FrontTextTerminalColor.UNDERLINE_ON}{FrontTextTerminalColor.MAGENTA}{messageString}{FrontTextTerminalColor.RESET}'))


def _createDir(path: str):
    os.makedirs(path, exist_ok=True)
    Path(f'{path}/__init__.py').touch()


# region jinja filters
def funcParamsJinjaFilter(value):
    res = map(lambda x: f'{Util.snakeCaseToLowerCameCaseString(x["name"])}: {x["type"]} = {x["default"]}', value)
    return ', '.join(list(res))


def funcArgsLowerKeyJinjaFilter(value, objectName=None, objectType=None, sign='='):
    if objectName is not None:
        if objectType == 'function':
            res = map(lambda
                          x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}.{x["name"]}()',
                      value)
        elif objectType == 'dictionary':
            res = map(lambda
                          x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}["{x["name"]}"]',
                      value)
        else:
            res = map(lambda
                          x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}.{x["name"]}',
                      value)
    else:
        res = map(lambda x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{x["name"]}', value)
    return ', '.join(list(res))


def funcArgsLowerValueJinjaFilter(value, objectName=None, objectType=None, sign='='):
    if objectName is not None:
        if objectType == 'function':
            res = map(lambda
                          x: f'{_argKey(x["name"], sign)}{sign}{objectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}()',
                      value)
        elif objectType == 'dictionary':
            res = map(lambda
                          x: f'{_argKey(x["name"], sign)}{sign}{objectName}["{Util.snakeCaseToLowerCameCaseString(x["name"])}"]',
                      value)
        else:
            res = map(lambda
                          x: f'{_argKey(x["name"], sign)}{sign}{objectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}',
                      value)
    else:
        res = map(lambda x: f'{_argKey(x["name"], sign)}{sign}{Util.snakeCaseToLowerCameCaseString(x["name"])}', value)
    return ', '.join(list(res))


def funcArgsJinjaFilter(value, objectName=None, objectType=None, sign='='):
    if objectName is not None:
        if objectType == 'function':
            res = map(lambda x: f'{_argKey(x["name"], sign)}{sign}{objectName}.{x["name"]}()', value)
        elif objectType == 'dictionary':
            res = map(lambda x: f'{_argKey(x["name"], sign)}{sign}{objectName}["{x["name"]}"]', value)
        else:
            res = map(lambda x: f'{_argKey(x["name"], sign)}{sign}{objectName}.{x["name"]}', value)
    else:
        res = map(lambda x: f'{_argKey(x["name"], sign)}{sign}{x["name"]}', value)
    return ', '.join(list(res))


def funcArgsLowerCamelCaseJinjaFilter(value, objectName=None, objectType=None, sign='='):
    if objectName is not None:
        if objectType == 'function':
            res = map(lambda
                          x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}()',
                      value)
        elif objectType == 'dictionary':
            res = map(lambda
                          x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}["{Util.snakeCaseToLowerCameCaseString(x["name"])}"]',
                      value)
        else:
            res = map(lambda
                          x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{objectName}.{Util.snakeCaseToLowerCameCaseString(x["name"])}',
                      value)
    else:
        res = map(lambda
                      x: f'{_argKey(Util.snakeCaseToLowerCameCaseString(x["name"]), sign)}{sign}{Util.snakeCaseToLowerCameCaseString(x["name"])}',
                  value)
    return ', '.join(list(res))


def _argKey(string: str, sign: str):
    return f'"{string}"' if sign == ':' else string


def funcToMapReturnDataJinjaFilter(value):
    res = map(lambda x: f"'{x['name']}': self.{Util.snakeCaseToLowerCameCaseString(x['name'])}()", value)
    return ', '.join(list(res))


def funcMapCompareJinjaFilter(value):
    res = map(lambda
                  x: f"self.{Util.snakeCaseToLowerCameCaseString(x['name'])}() == other.{Util.snakeCaseToLowerCameCaseString(x['name'])}()",
              value)
    return ' and '.join(list(res))


# endregion


initGlobalConfig()
fileLoader = FileSystemLoader(Config.templatePath)
jinjaEnv = Environment(loader=fileLoader)
jinjaEnv.filters['mapFuncParams'] = funcParamsJinjaFilter
jinjaEnv.filters['mapFuncArgs'] = funcArgsJinjaFilter
jinjaEnv.filters['mapFuncArgsLowerKey'] = funcArgsLowerKeyJinjaFilter
jinjaEnv.filters['mapFuncArgsLowerValue'] = funcArgsLowerValueJinjaFilter
jinjaEnv.filters['mapFuncArgsLowerCase'] = funcArgsLowerCamelCaseJinjaFilter
jinjaEnv.filters['mapFunToMapReturnData'] = funcToMapReturnDataJinjaFilter
jinjaEnv.filters['mapFunCompare'] = funcMapCompareJinjaFilter
jinjaEnv.filters['spacedWords'] = lambda x: Util.snakeCaseToLowerSpacedWordsString(string=x)
jinjaEnv.filters['upperCamelCase'] = lambda x: Util.snakeCaseToUpperCameCaseString(string=x)
jinjaEnv.filters['lowerCamelCase'] = lambda x: Util.snakeCaseToLowerCameCaseString(string=x)

if __name__ == '__main__':
    cli()

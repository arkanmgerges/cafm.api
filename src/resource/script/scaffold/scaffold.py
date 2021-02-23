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
import yaml
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from src.resource.common.Util import Util


# region Global config & settings
class TerminalColor:
    BLUE = "\x1b[34;21m"
    GREEN = "\x1b[32;21m"
    YELLOW = "\x1b[33;21m"
    RED = "\x1b[31;21m"
    RESET = "\x1b[0m"


class Config:
    configData = None
    projectPath = None
    templatePath = None
    configFilePath = None

    @staticmethod
    def __repr__():
        return f'{TerminalColor.GREEN}projectPath:{TerminalColor.RESET} {Config.projectPath}\n' \
               f'{TerminalColor.GREEN}templatePath:{TerminalColor.RESET} {Config.templatePath}\n' \
               f'{TerminalColor.GREEN}configFilePath:{TerminalColor.RESET} {Config.configFilePath}\n' \
               f'{TerminalColor.GREEN}configData:{TerminalColor.RESET} {json.dumps(Config.configData, indent=2)}\n'


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
    protoPath = Config.configData['global']['path']['proto_buffer']
    protoFullPath = f'{Config.projectPath}/{protoPath}'
    _createDir(path=protoFullPath)
    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        doNotSkip = True if ('skip' in model and 'proto' not in model['skip']) or ('skip' not in model) else False
        if doNotSkip:
            modelProtoName = f'{protoFullPath}/{model["microservice"]}/{model["name"]}'
            modelTemplate = jinjaEnv.get_template(f'proto/model.jinja2')
            modelAppTemplate = jinjaEnv.get_template(f'proto/model_app.jinja2')
            with open(f'{modelProtoName}.proto', 'w+') as file:
                file.write(modelTemplate.render(model=model))
                file.write('\n')
            with open(f'{modelProtoName}_app_service.proto', 'w+') as file:
                file.write(modelAppTemplate.render(model=model))
                file.write('\n')


# Generate routes for the models
def generateRoute():
    routerPath = Config.configData['global']['path']['router']
    routerFullPath = f'{Config.projectPath}/{routerPath}'
    _createDir(path=routerFullPath)
    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        _createDir(f'{routerFullPath}/{model["path"]}')
        doNotSkip = True if ('skip' in model and 'router' not in model['skip']) or ('skip' not in model) else False
        if doNotSkip:
            modelTestName = f'{routerFullPath}/{model["path"]}/{model["name"]}'
            testTemplate = jinjaEnv.get_template(f'router/model.jinja2')
            with open(f'{modelTestName}.py', 'w+') as file:
                file.write(testTemplate.render(model=model))
                file.write('\n')


# Generate api response models
def generateRouterModelResponse():
    modelResponsePath = Config.configData['global']['path']['router_model_response']
    modelResponseFullPath = f'{Config.projectPath}/{modelResponsePath}'
    _createDir(path=modelResponseFullPath)
    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        _createDir(f'{modelResponseFullPath}/{model["path"]}')
        doNotSkip = True if ('skip' in model and 'model_response' not in model['skip']) or (
                'skip' not in model) else False
        if doNotSkip:
            modelTestName = f'{modelResponseFullPath}/{model["path"]}/{Util.snakeCaseToUpperCameCaseString(model["name"])}'
            template = jinjaEnv.get_template(f'router/model_response/model.jinja2')
            with open(f'{modelTestName}.py', 'w+') as file:
                file.write(template.render(model=model))
                file.write('\n')
            template = jinjaEnv.get_template(f'router/model_response/models.jinja2')
            with open(f'{modelTestName}s.py', 'w+') as file:
                file.write(template.render(model=model))
                file.write('\n')


# Generate grpc client files
def generateGrpcApiClient():
    grpcClientPath = Config.configData['global']['path']['grpc_api_client']
    grpcClientFullPath = f'{Config.projectPath}/{grpcClientPath}'
    _createDir(path=grpcClientFullPath)
    for modelConfig in Config.configData['domain_model']:
        model = modelConfig['model']
        _createDir(f'{grpcClientFullPath}/{model["path"]}')
        doNotSkip = True if ('skip' in model and 'grpc_client' not in model['skip']) or ('skip' not in model) else False
        if doNotSkip:
            modelTestName = f'{grpcClientFullPath}/{model["path"]}/{Util.snakeCaseToUpperCameCaseString(model["name"])}'
            template = jinjaEnv.get_template(f'grpc/model.jinja2')
            with open(f'{modelTestName}Client.py', 'w+') as file:
                file.write(template.render(model=model))
                file.write('\n')


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

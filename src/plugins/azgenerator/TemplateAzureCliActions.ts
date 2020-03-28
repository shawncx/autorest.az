﻿/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

import { CodeModelAz } from "./CodeModelAz"
import { ToCamelCase, Capitalize } from "../../utils/helper";
import { SchemaType, Parameter } from "@azure-tools/codemodel";
import { stringify } from "querystring";
import { HeaderGenerator } from "./Header";
import { isNullOrUndefined } from "util";

export function GenerateAzureCliActions(model: CodeModelAz): string[] {
    let header: HeaderGenerator = new HeaderGenerator();

    header.addImport("argparse");
    header.addFromImport("knack.util", ["CLIError"]);
    header.disableProtectedAccess = true;
    let allActions: Map<string, boolean> = new Map<string, boolean>();

    let output: string[] = header.getLines();

    if (model.SelectFirstCommandGroup()) {
        do {
            if (model.SelectFirstCommand()) {
                do {
                    if (model.SelectFirstMethod()) {
                        do {
                            if (model.SelectFirstMethodParameter()) {
                                do {
                                    let actionName = model.Parameter_ActionName(model.MethodParameter);
                                    if (isNullOrUndefined(actionName)) {
                                        continue;
                                    }
                                    
                                    if (allActions.has(actionName)) {
                                        continue;
                                    }
                                    allActions.set(actionName, true);
                            
                                    output.push("");
                                    output.push("");
                                    let baseAction = "Action";
                                    if (model.MethodParameter_Type == SchemaType.Array) baseAction = "_Append" + baseAction;
                                    output.push("class " + actionName + "(argparse." + baseAction + "):");
                                    output.push("    def __call__(self, parser, namespace, values, option_string=None):");
                                    output.push("        action = self.get_action(values, option_string)");
                                    if (model.MethodParameter_Type == SchemaType.Array) {
                                        output.push("        super(" + actionName + ", self).__call__(parser, namespace, action, option_string)");
                                    } else {
                                        output.push("        namespace." + model.MethodParameter_MapsTo.toLowerCase().replace(/-/g, '_') + " = action");
                                    }

                                    output.push("");
                                    output.push("    def get_action(self, values, option_string):  # pylint: disable=no-self-use");
                                    output.push("        try:");
                                    output.push("            properties = dict(x.split('=', 1) for x in values)");
                                    output.push("        except ValueError:");
                                    output.push("            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))");
                                    output.push("        d = {}");
                                    output.push("        for k in properties:");
                                    output.push("            kl = k.lower()");
                                    output.push("            v = properties[k]");
                                    let foundProperties = false;
                                    let preParamType = model.MethodParameter_Type;
                                    if (model.EnterSubMethodParameters()) {
                                        if (model.SelectFirstMethodParameter()) {
                                            foundProperties = true;
                                            let ifkv = "if";
                                            do {
                                                if (model.SubMethodParameter['readOnly']) {
                                                    continue;
                                                }
                                                if (model.SubMethodParameter['schema']?.type == SchemaType.Constant) {
                                                    continue;
                                                }
                                                output.push("            " + ifkv + " kl == '" + model.MethodParameter_NameAz + "':");
                                                output.push("                d['" + model.MethodParameter_NamePython + "'] = v");
                                                ifkv = "elif";
                                            } while (model.SelectNextMethodParameter());
                                        }
                                    }
                                    model.ExitSubMethodParameters();
                                    if (!foundProperties && preParamType == SchemaType.Dictionary) {
                                        output.push("            d[k] = v");
                                    }
                                    output.push("        return d");

                                } while (model.SelectNextMethodParameter());
                            }
                        } while (model.SelectNextMethod());
                    }
                } while (model.SelectNextCommand());
            }
        } while (model.SelectNextCommandGroup());
    }

    output.push("");

    return output;
}



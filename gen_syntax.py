#!/usr/bin/env python
import sys, os, os.path
import numpy as np
import plistlib
import simplejson

filename = "fei.JSON-tmLanguage"

frst_lvl_kywds  = "\\\\b(";
scnd_lvl_kywds = "\\\\b(";

with open("./snippets/First_Level_Keywords.txt") as f:
    for line in f:
        frst_lvl_kywds  = frst_lvl_kywds + line.rstrip() + "|";

with open("./snippets/Second_Level_Keywords.txt") as f:
    for line in f:
        scnd_lvl_kywds  = scnd_lvl_kywds + line.rstrip() + "|";

frst_lvl_kywds  =  frst_lvl_kywds  + ")\\\\b";
scnd_lvl_kywds =  scnd_lvl_kywds + ")\\\\b";

fei_syntax = open(filename,'w')

fei_syntax.writelines(""" \
// [PackageDev] target_format: plist, ext: tmLanguage                                                           \n \
{ "name": "fei",                                                                                                \n \
  "scopeName": "source.fei",                                                                                    \n \
  "fileTypes": ["fei", "essi"],                                                                                 \n \
  "foldingStartMarker": ".*[^;]|{",                                                                             \n \
  "foldingStopMarker": ";|}",                                                                                   \n \
  "patterns": [                                                                                                 \n \
        { "match": "//.*",                                                                                      \n \
          "name": "comment.line.double-slash",                                                                  \n \
          "comment": "Comments"                                                                                 \n \
        },                                                                                                      \n \
        { "match": "if|while|else",                                                                             \n \
          "name": "keyword.control.fei",                                                                        \n \
          "comment": "If "                                                                                      \n \
        },                                                                                                      \n \
        //{ "match": " """ + frst_lvl_kywds + """ ",                                                            \n \
        //  "name": "keyword.other.fei",                                                                        \n \
        //  "comment": "FEI reserved 1st-lvl keywords"                                                          \n \
        //},                                                                                                    \n \
        /*{ "match": "(GPa|Hz|Km|MPa|N|Pa|cm|g|kN|kPa|kg|m|mm|ms|ns|pi|s)&&(^([A-Za-z_][A-Za-z0-9_]+))",        \n \
          "name": "constant.language.fei",                                                                      \n \
          "comment": "Units!!"                                                                                  \n \
        },*/                                                                                                    \n \
        { "match": " """ + scnd_lvl_kywds + """ ",                                                              \n \
          "name": "constant.other.fei",                                                                         \n \
          "comment": "FEI reserved 2st-lvl keywords"                                                            \n \
        },                                                                                                      \n \
        { "match": "[A-Za-z_][A-Za-z0-9_]+",                                                                    \n \
         "name": "variable.other.fei",                                                                          \n \
         "comment": "Variables like a, x, sigma_xx, Sigma_XY..."                                                \n \
        },                                                                                                      \n \
        { "match": "[0-9]+\\\\.[0-9]*([Ee][-+]?[0-9]+)?|(\\\\.)?[0-9]+([Ee][-+]?[0-9]+)?",                      \n \
          "name": "constant.numeric.fei",                                                                       \n \
          "comment": "Numbers like 1, 1.0, 1.2e2, 1.2e+3, 1.2e-3, .1, .1e+3, .1e-3, .1e2"                       \n \
        },                                                                                                      \n \
        { "match": "(\\")+(.*)(\\")+",                                                                          \n \
          "name": "string.quoted.double",                                                                       \n \
          "comment": "Strings"                                                                                  \n \
        }                                                                                                       \n \
    ],                                                                                                          \n \
    "uuid": "f2c2f4ff-2592-4649-b8ba-3ecf8faaf57c"                                                              \n \
}                                                                                                               \n \
""")

fei_syntax.close();

# fei_syntax = open(filename,'r');
# json_file_content = fei_syntax.read();

# # Now convert JSON to PLIST
# converted_dict = simplejson.loads(json_file_content);
# # plistlib.writePlist(converted_dict, "fei.tmlLanguage")
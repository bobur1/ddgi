"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

/*!
* inputmask.extensions.min.js
* https://github.com/RobinHerbots/Inputmask
* Copyright (c) 2010 - 2019 Robin Herbots
* Licensed under the MIT license (http://www.opensource.org/licenses/mit-license.php)
* Version: 4.0.9
*/
(function (factory) {
  if (typeof define === "function" && define.amd) {
    define(["./inputmask"], factory);
  } else if ((typeof exports === "undefined" ? "undefined" : _typeof(exports)) === "object") {
    module.exports = factory(require("./inputmask"));
  } else {
    factory(window.Inputmask);
  }
})(function (Inputmask) {
  Inputmask.extendDefinitions({
    A: {
      validator: "[A-Za-z\u0410-\u044F\u0401\u0451\xC0-\xFF\xB5]",
      casing: "upper"
    },
    "&": {
      validator: "[0-9A-Za-z\u0410-\u044F\u0401\u0451\xC0-\xFF\xB5]",
      casing: "upper"
    },
    "#": {
      validator: "[0-9A-Fa-f]",
      casing: "upper"
    }
  });
  Inputmask.extendAliases({
    cssunit: {
      regex: "[+-]?[0-9]+\\.?([0-9]+)?(px|em|rem|ex|%|in|cm|mm|pt|pc)"
    },
    url: {
      regex: "(https?|ftp)//.*",
      autoUnmask: false
    },
    ip: {
      mask: "i[i[i]].i[i[i]].i[i[i]].i[i[i]]",
      definitions: {
        i: {
          validator: function validator(chrs, maskset, pos, strict, opts) {
            if (pos - 1 > -1 && maskset.buffer[pos - 1] !== ".") {
              chrs = maskset.buffer[pos - 1] + chrs;

              if (pos - 2 > -1 && maskset.buffer[pos - 2] !== ".") {
                chrs = maskset.buffer[pos - 2] + chrs;
              } else chrs = "0" + chrs;
            } else chrs = "00" + chrs;

            return new RegExp("25[0-5]|2[0-4][0-9]|[01][0-9][0-9]").test(chrs);
          }
        }
      },
      onUnMask: function onUnMask(maskedValue, unmaskedValue, opts) {
        return maskedValue;
      },
      inputmode: "numeric"
    },
    email: {
      mask: "*{1,64}[.*{1,64}][.*{1,64}][.*{1,63}]@-{1,63}.-{1,63}[.-{1,63}][.-{1,63}]",
      greedy: false,
      casing: "lower",
      onBeforePaste: function onBeforePaste(pastedValue, opts) {
        pastedValue = pastedValue.toLowerCase();
        return pastedValue.replace("mailto:", "");
      },
      definitions: {
        "*": {
          validator: "[0-9\uFF11-\uFF19A-Za-z\u0410-\u044F\u0401\u0451\xC0-\xFF\xB5!#$%&'*+/=?^_`{|}~-]"
        },
        "-": {
          validator: "[0-9A-Za-z-]"
        }
      },
      onUnMask: function onUnMask(maskedValue, unmaskedValue, opts) {
        return maskedValue;
      },
      inputmode: "email"
    },
    mac: {
      mask: "##:##:##:##:##:##"
    },
    vin: {
      mask: "V{13}9{4}",
      definitions: {
        V: {
          validator: "[A-HJ-NPR-Za-hj-npr-z\\d]",
          casing: "upper"
        }
      },
      clearIncomplete: true,
      autoUnmask: true
    }
  });
  return Inputmask;
});
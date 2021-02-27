"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

/*!
* global/window.js
* https://github.com/RobinHerbots/Inputmask
* Copyright (c) 2010 - 2019 Robin Herbots
* Licensed under the MIT license (http://www.opensource.org/licenses/mit-license.php)
* Version: 4.0.9
*/
if (typeof define === "function" && define.amd) define(function () {
  return typeof window !== "undefined" ? window : new (eval("require('jsdom').JSDOM"))("").window;
});else if ((typeof exports === "undefined" ? "undefined" : _typeof(exports)) === "object") module.exports = typeof window !== "undefined" ? window : new (eval("require('jsdom').JSDOM"))("").window;
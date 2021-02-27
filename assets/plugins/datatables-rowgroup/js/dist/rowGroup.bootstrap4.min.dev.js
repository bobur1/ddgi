"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

/*!
 Bootstrap 4 styling wrapper for RowGroup
 ©2018 SpryMedia Ltd - datatables.net/license
*/
(function (c) {
  "function" === typeof define && define.amd ? define(["jquery", "datatables.net-bs4", "datatables.net-rowgroup"], function (a) {
    return c(a, window, document);
  }) : "object" === (typeof exports === "undefined" ? "undefined" : _typeof(exports)) ? module.exports = function (a, b) {
    a || (a = window);
    if (!b || !b.fn.dataTable) b = require("datatables.net-bs4")(a, b).$;
    b.fn.dataTable.RowGroup || require("datatables.net-rowgroup")(a, b);
    return c(b, a, a.document);
  } : c(jQuery, window, document);
})(function (c) {
  return c.fn.dataTable;
});
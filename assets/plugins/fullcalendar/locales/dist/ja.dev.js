"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.ja = factory()));
})(void 0, function () {
  'use strict';

  var ja = {
    code: "ja",
    buttonText: {
      prev: "前",
      next: "次",
      today: "今日",
      month: "月",
      week: "週",
      day: "日",
      list: "予定リスト"
    },
    weekLabel: "週",
    allDayText: "終日",
    eventLimitText: function eventLimitText(n) {
      return "他 " + n + " 件";
    },
    noEventsMessage: "表示する予定はありません"
  };
  return ja;
});
"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales['zh-tw'] = factory()));
})(void 0, function () {
  'use strict';

  var zhTw = {
    code: "zh-tw",
    buttonText: {
      prev: "上月",
      next: "下月",
      today: "今天",
      month: "月",
      week: "週",
      day: "天",
      list: "活動列表"
    },
    weekLabel: "周",
    allDayText: "整天",
    eventLimitText: '顯示更多',
    noEventsMessage: "没有任何活動"
  };
  return zhTw;
});
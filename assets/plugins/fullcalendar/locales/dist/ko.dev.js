"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.ko = factory()));
})(void 0, function () {
  'use strict';

  var ko = {
    code: "ko",
    buttonText: {
      prev: "이전달",
      next: "다음달",
      today: "오늘",
      month: "월",
      week: "주",
      day: "일",
      list: "일정목록"
    },
    weekLabel: "주",
    allDayText: "종일",
    eventLimitText: "개",
    noEventsMessage: "일정이 없습니다"
  };
  return ko;
});
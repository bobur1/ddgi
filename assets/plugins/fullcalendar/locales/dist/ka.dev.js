"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.ka = factory()));
})(void 0, function () {
  'use strict';

  var ka = {
    code: "ka",
    week: {
      dow: 1,
      doy: 7
    },
    buttonText: {
      prev: "წინა",
      next: "შემდეგი",
      today: "დღეს",
      month: "თვე",
      week: "კვირა",
      day: "დღე",
      list: "დღის წესრიგი"
    },
    weekLabel: "კვ",
    allDayText: "მთელი დღე",
    eventLimitText: function eventLimitText(n) {
      return "+ კიდევ " + n;
    },
    noEventsMessage: "ღონისძიებები არ არის"
  };
  return ka;
});
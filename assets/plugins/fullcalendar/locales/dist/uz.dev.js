"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.uz = factory()));
})(void 0, function () {
  'use strict';

  var uz = {
    code: "uz",
    buttonText: {
      month: "Oy",
      week: "Xafta",
      day: "Kun",
      list: "Kun tartibi"
    },
    allDayText: "Kun bo'yi",
    eventLimitText: function eventLimitText(n) {
      return "+ yana " + n;
    },
    noEventsMessage: "Ko'rsatish uchun voqealar yo'q"
  };
  return uz;
});
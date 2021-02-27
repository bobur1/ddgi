"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales.th = factory()));
})(void 0, function () {
  'use strict';

  var th = {
    code: "th",
    week: {
      dow: 1,
      doy: 4 // The week that contains Jan 4th is the first week of the year.

    },
    buttonText: {
      prev: "ก่อนหน้า",
      next: "ถัดไป",
      prevYear: 'ปีก่อนหน้า',
      nextYear: 'ปีถัดไป',
      year: 'ปี',
      today: "วันนี้",
      month: "เดือน",
      week: "สัปดาห์",
      day: "วัน",
      list: "กำหนดการ"
    },
    weekLabel: "สัปดาห์",
    allDayText: "ตลอดวัน",
    eventLimitText: "เพิ่มเติม",
    noEventsMessage: "ไม่มีกิจกรรมที่จะแสดง"
  };
  return th;
});
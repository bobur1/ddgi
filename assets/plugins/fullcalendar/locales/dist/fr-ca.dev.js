"use strict";

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

(function (global, factory) {
  (typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object' && typeof module !== 'undefined' ? module.exports = factory() : typeof define === 'function' && define.amd ? define(factory) : (global = global || self, (global.FullCalendarLocales = global.FullCalendarLocales || {}, global.FullCalendarLocales['fr-ca'] = factory()));
})(void 0, function () {
  'use strict';

  var frCa = {
    code: "fr",
    buttonText: {
      prev: "Précédent",
      next: "Suivant",
      today: "Aujourd'hui",
      year: "Année",
      month: "Mois",
      week: "Semaine",
      day: "Jour",
      list: "Mon planning"
    },
    weekLabel: "Sem.",
    allDayHtml: "Toute la<br/>journée",
    eventLimitText: "en plus",
    noEventsMessage: "Aucun événement à afficher"
  };
  return frCa;
});
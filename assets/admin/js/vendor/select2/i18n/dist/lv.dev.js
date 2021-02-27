"use strict";

/*! Select2 4.0.7 | https://github.com/select2/select2/blob/master/LICENSE.md */
(function () {
  if (jQuery && jQuery.fn && jQuery.fn.select2 && jQuery.fn.select2.amd) var e = jQuery.fn.select2.amd;
  return e.define("select2/i18n/lv", [], function () {
    function e(e, t, n, r) {
      return e === 11 ? t : e % 10 === 1 ? n : r;
    }

    return {
      inputTooLong: function inputTooLong(t) {
        var n = t.input.length - t.maximum,
            r = "Lūdzu ievadiet par  " + n;
        return r += " simbol" + e(n, "iem", "u", "iem"), r + " mazāk";
      },
      inputTooShort: function inputTooShort(t) {
        var n = t.minimum - t.input.length,
            r = "Lūdzu ievadiet vēl " + n;
        return r += " simbol" + e(n, "us", "u", "us"), r;
      },
      loadingMore: function loadingMore() {
        return "Datu ielāde…";
      },
      maximumSelected: function maximumSelected(t) {
        var n = "Jūs varat izvēlēties ne vairāk kā " + t.maximum;
        return n += " element" + e(t.maximum, "us", "u", "us"), n;
      },
      noResults: function noResults() {
        return "Sakritību nav";
      },
      searching: function searching() {
        return "Meklēšana…";
      },
      removeAllItems: function removeAllItems() {
        return "Noņemt visus vienumus";
      }
    };
  }), {
    define: e.define,
    require: e.require
  };
})();
"use strict";

/*! Select2 4.0.7 | https://github.com/select2/select2/blob/master/LICENSE.md */
(function () {
  if (jQuery && jQuery.fn && jQuery.fn.select2 && jQuery.fn.select2.amd) var e = jQuery.fn.select2.amd;
  return e.define("select2/i18n/dsb", [], function () {
    var e = ["znamuško", "znamušce", "znamuška", "znamuškow"],
        t = ["zapisk", "zapiska", "zapiski", "zapiskow"],
        n = function n(t, _n) {
      if (t === 1) return _n[0];
      if (t === 2) return _n[1];
      if (t > 2 && t <= 4) return _n[2];
      if (t >= 5) return _n[3];
    };

    return {
      errorLoading: function errorLoading() {
        return "Wuslědki njejsu se dali zacytaś.";
      },
      inputTooLong: function inputTooLong(t) {
        var r = t.input.length - t.maximum;
        return "Pšosym lašuj " + r + " " + n(r, e);
      },
      inputTooShort: function inputTooShort(t) {
        var r = t.minimum - t.input.length;
        return "Pšosym zapódaj nanejmjenjej " + r + " " + n(r, e);
      },
      loadingMore: function loadingMore() {
        return "Dalšne wuslědki se zacytaju…";
      },
      maximumSelected: function maximumSelected(e) {
        return "Móžoš jano " + e.maximum + " " + n(e.maximum, t) + "wubraś.";
      },
      noResults: function noResults() {
        return "Žedne wuslědki namakane";
      },
      searching: function searching() {
        return "Pyta se…";
      },
      removeAllItems: function removeAllItems() {
        return "Remove all items";
      }
    };
  }), {
    define: e.define,
    require: e.require
  };
})();
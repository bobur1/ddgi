"use strict";

/*! Select2 4.0.7 | https://github.com/select2/select2/blob/master/LICENSE.md */
(function () {
  if (jQuery && jQuery.fn && jQuery.fn.select2 && jQuery.fn.select2.amd) var e = jQuery.fn.select2.amd;
  return e.define("select2/i18n/hsb", [], function () {
    var e = ["znamješko", "znamješce", "znamješka", "znamješkow"],
        t = ["zapisk", "zapiskaj", "zapiski", "zapiskow"],
        n = function n(t, _n) {
      if (t === 1) return _n[0];
      if (t === 2) return _n[1];
      if (t > 2 && t <= 4) return _n[2];
      if (t >= 5) return _n[3];
    };

    return {
      errorLoading: function errorLoading() {
        return "Wuslědki njedachu so začitać.";
      },
      inputTooLong: function inputTooLong(t) {
        var r = t.input.length - t.maximum;
        return "Prošu zhašej " + r + " " + n(r, e);
      },
      inputTooShort: function inputTooShort(t) {
        var r = t.minimum - t.input.length;
        return "Prošu zapodaj znajmjeńša " + r + " " + n(r, e);
      },
      loadingMore: function loadingMore() {
        return "Dalše wuslědki so začitaja…";
      },
      maximumSelected: function maximumSelected(e) {
        return "Móžeš jenož " + e.maximum + " " + n(e.maximum, t) + "wubrać";
      },
      noResults: function noResults() {
        return "Žane wuslědki namakane";
      },
      searching: function searching() {
        return "Pyta so…";
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
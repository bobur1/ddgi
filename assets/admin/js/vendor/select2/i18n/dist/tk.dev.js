"use strict";

/*! Select2 4.0.7 | https://github.com/select2/select2/blob/master/LICENSE.md */
(function () {
  if (jQuery && jQuery.fn && jQuery.fn.select2 && jQuery.fn.select2.amd) var e = jQuery.fn.select2.amd;
  return e.define("select2/i18n/tk", [], function () {
    return {
      errorLoading: function errorLoading() {
        return "Netije ýüklenmedi.";
      },
      inputTooLong: function inputTooLong(e) {
        var t = e.input.length - e.maximum,
            n = t + " harp bozuň.";
        return n;
      },
      inputTooShort: function inputTooShort(e) {
        var t = e.minimum - e.input.length,
            n = "Ýene-de iň az " + t + " harp ýazyň.";
        return n;
      },
      loadingMore: function loadingMore() {
        return "Köpräk netije görkezilýär…";
      },
      maximumSelected: function maximumSelected(e) {
        var t = "Diňe " + e.maximum + " sanysyny saýlaň.";
        return t;
      },
      noResults: function noResults() {
        return "Netije tapylmady.";
      },
      searching: function searching() {
        return "Gözlenýär…";
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
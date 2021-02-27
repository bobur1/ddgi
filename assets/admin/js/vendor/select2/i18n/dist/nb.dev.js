"use strict";

/*! Select2 4.0.7 | https://github.com/select2/select2/blob/master/LICENSE.md */
(function () {
  if (jQuery && jQuery.fn && jQuery.fn.select2 && jQuery.fn.select2.amd) var e = jQuery.fn.select2.amd;
  return e.define("select2/i18n/nb", [], function () {
    return {
      errorLoading: function errorLoading() {
        return "Kunne ikke hente resultater.";
      },
      inputTooLong: function inputTooLong(e) {
        var t = e.input.length - e.maximum;
        return "Vennligst fjern " + t + " tegn";
      },
      inputTooShort: function inputTooShort(e) {
        var t = e.minimum - e.input.length;
        return "Vennligst skriv inn " + t + " tegn til";
      },
      loadingMore: function loadingMore() {
        return "Laster flere resultater…";
      },
      maximumSelected: function maximumSelected(e) {
        return "Du kan velge maks " + e.maximum + " elementer";
      },
      noResults: function noResults() {
        return "Ingen treff";
      },
      searching: function searching() {
        return "Søker…";
      },
      removeAllItems: function removeAllItems() {
        return "Fjern alle elementer";
      }
    };
  }), {
    define: e.define,
    require: e.require
  };
})();
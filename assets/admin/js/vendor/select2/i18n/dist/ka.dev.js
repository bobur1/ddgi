"use strict";

/*! Select2 4.0.7 | https://github.com/select2/select2/blob/master/LICENSE.md */
(function () {
  if (jQuery && jQuery.fn && jQuery.fn.select2 && jQuery.fn.select2.amd) var e = jQuery.fn.select2.amd;
  return e.define("select2/i18n/ka", [], function () {
    return {
      errorLoading: function errorLoading() {
        return "მონაცემების ჩატვირთვა შეუძლებელია.";
      },
      inputTooLong: function inputTooLong(e) {
        var t = e.input.length - e.maximum,
            n = "გთხოვთ აკრიფეთ " + t + " სიმბოლოთი ნაკლები";
        return n;
      },
      inputTooShort: function inputTooShort(e) {
        var t = e.minimum - e.input.length,
            n = "გთხოვთ აკრიფეთ " + t + " სიმბოლო ან მეტი";
        return n;
      },
      loadingMore: function loadingMore() {
        return "მონაცემების ჩატვირთვა…";
      },
      maximumSelected: function maximumSelected(e) {
        var t = "თქვენ შეგიძლიათ აირჩიოთ არაუმეტეს " + e.maximum + " ელემენტი";
        return t;
      },
      noResults: function noResults() {
        return "რეზულტატი არ მოიძებნა";
      },
      searching: function searching() {
        return "ძიება…";
      },
      removeAllItems: function removeAllItems() {
        return "ამოიღე ყველა ელემენტი";
      }
    };
  }), {
    define: e.define,
    require: e.require
  };
})();
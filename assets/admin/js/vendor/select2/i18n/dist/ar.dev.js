"use strict";

/*! Select2 4.0.7 | https://github.com/select2/select2/blob/master/LICENSE.md */
(function () {
  if (jQuery && jQuery.fn && jQuery.fn.select2 && jQuery.fn.select2.amd) var e = jQuery.fn.select2.amd;
  return e.define("select2/i18n/ar", [], function () {
    return {
      errorLoading: function errorLoading() {
        return "لا يمكن تحميل النتائج";
      },
      inputTooLong: function inputTooLong(e) {
        var t = e.input.length - e.maximum;
        return "الرجاء حذف " + t + " عناصر";
      },
      inputTooShort: function inputTooShort(e) {
        var t = e.minimum - e.input.length;
        return "الرجاء إضافة " + t + " عناصر";
      },
      loadingMore: function loadingMore() {
        return "جاري تحميل نتائج إضافية...";
      },
      maximumSelected: function maximumSelected(e) {
        return "تستطيع إختيار " + e.maximum + " بنود فقط";
      },
      noResults: function noResults() {
        return "لم يتم العثور على أي نتائج";
      },
      searching: function searching() {
        return "جاري البحث…";
      },
      removeAllItems: function removeAllItems() {
        return "قم بإزالة كل العناصر";
      }
    };
  }), {
    define: e.define,
    require: e.require
  };
})();
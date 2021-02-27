"use strict";

/*! Select2 4.0.7 | https://github.com/select2/select2/blob/master/LICENSE.md */
(function () {
  if (jQuery && jQuery.fn && jQuery.fn.select2 && jQuery.fn.select2.amd) var e = jQuery.fn.select2.amd;
  return e.define("select2/i18n/zh-CN", [], function () {
    return {
      errorLoading: function errorLoading() {
        return "无法载入结果。";
      },
      inputTooLong: function inputTooLong(e) {
        var t = e.input.length - e.maximum,
            n = "请删除" + t + "个字符";
        return n;
      },
      inputTooShort: function inputTooShort(e) {
        var t = e.minimum - e.input.length,
            n = "请再输入至少" + t + "个字符";
        return n;
      },
      loadingMore: function loadingMore() {
        return "载入更多结果…";
      },
      maximumSelected: function maximumSelected(e) {
        var t = "最多只能选择" + e.maximum + "个项目";
        return t;
      },
      noResults: function noResults() {
        return "未找到结果";
      },
      searching: function searching() {
        return "搜索中…";
      },
      removeAllItems: function removeAllItems() {
        return "删除所有项目";
      }
    };
  }), {
    define: e.define,
    require: e.require
  };
})();
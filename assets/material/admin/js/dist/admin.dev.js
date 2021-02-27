"use strict";

(function ($) {
  var toasts = ['success', 'warning', 'info', 'error'];
  $('#mobile-demo').on('touchstart click touchmove', function () {
    $('.scroll-pane').jScrollPane();
  });
  $('.collapsible-body, .collapsible-header').on('mouseenter', function () {
    $('.scroll-pane').jScrollPane();
  });
  $('#side-bar').on('mouseenter scroll', function () {
    $('.scroll-pane').jScrollPane();
  }).mouseleave(function () {
    var jsp = $('.scroll-pane').data('jsp');

    if (jsp) {
      jsp.destroy();
    }
  });
  $('.collapsible-body > .active').closest('.scrollspy').addClass('active');
  window.addEventListener('load', function () {
    var collapsible = document.querySelectorAll('.collapsible:not(.no-autoinit)');
    M.Collapsible.init(collapsible, {
      accordion: false
    });
    var sidenav = document.querySelectorAll('.sidenav:not(.no-autoinit)');
    M.Sidenav.init(sidenav);
    var elems = document.querySelectorAll('.dropdown-trigger:not(.no-autoinit)');
    M.Dropdown.init(elems);
    $('select').not('.empty-form select, .selector-available select, .selector-chosen select, .admin-autocomplete, .no-autoinit').formSelect();
    var _iteratorNormalCompletion = true;
    var _didIteratorError = false;
    var _iteratorError = undefined;

    try {
      for (var _iterator = toasts[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
        var toast = _step.value;
        var messages = $(".messagelist > .".concat(toast));
        var _iteratorNormalCompletion2 = true;
        var _didIteratorError2 = false;
        var _iteratorError2 = undefined;

        try {
          for (var _iterator2 = messages[Symbol.iterator](), _step2; !(_iteratorNormalCompletion2 = (_step2 = _iterator2.next()).done); _iteratorNormalCompletion2 = true) {
            var message = _step2.value;
            M.toast({
              html: message.innerText,
              classes: "rounded ".concat(toast, "-toast")
            });
          }
        } catch (err) {
          _didIteratorError2 = true;
          _iteratorError2 = err;
        } finally {
          try {
            if (!_iteratorNormalCompletion2 && _iterator2["return"] != null) {
              _iterator2["return"]();
            }
          } finally {
            if (_didIteratorError2) {
              throw _iteratorError2;
            }
          }
        }
      }
    } catch (err) {
      _didIteratorError = true;
      _iteratorError = err;
    } finally {
      try {
        if (!_iteratorNormalCompletion && _iterator["return"] != null) {
          _iterator["return"]();
        }
      } finally {
        if (_didIteratorError) {
          throw _iteratorError;
        }
      }
    }

    $('img[src$="icon-yes.svg"]').replaceWith('<i class="material-icons green-color medium-icon">check_circle</i>');
    $('img[src$="icon-no.svg"]').replaceWith('<i class="material-icons red-color medium-icon">highlight_off</i>');
    $('img[src$="icon-unknown.svg"]').replaceWith('<i class="material-icons medium-icon">help_outline</i>');
  });
})(jQuery);
(self.webpackChunk_N_E = self.webpackChunk_N_E || []).push([[791], {
    28935: function(e, r, t) {
        "use strict";
        r.Z = function() {
            for (var e, r, t = 0, n = ""; t < arguments.length; )
                (e = arguments[t++]) && (r = function e(r) {
                    var t, n, i = "";
                    if ("string" == typeof r || "number" == typeof r)
                        i += r;
                    else if ("object" == typeof r) {
                        if (Array.isArray(r))
                            for (t = 0; t < r.length; t++)
                                r[t] && (n = e(r[t])) && (i && (i += " "),
                                i += n);
                        else
                            for (t in r)
                                r[t] && (i && (i += " "),
                                i += t)
                    }
                    return i
                }(e)) && (n && (n += " "),
                n += r);
            return n
        }
    },
    25458: function(e, r, t) {
        "use strict";
        var n, i;
        e.exports = (null == (n = t.g.process) ? void 0 : n.env) && "object" == typeof (null == (i = t.g.process) ? void 0 : i.env) ? t.g.process : t(73034)
    },
    57863: function(e, r, t) {
        Promise.resolve().then(t.bind(t, 56704))
    },
    56704: function(e, r, t) {
        "use strict";
        t.r(r),
        t.d(r, {
            default: function() {
                return f
            }
        });
        var n = t(15387)
          , i = t(51697)
          , o = t.n(i)
          , s = t(28935)
          , a = t(81600)
          , c = t(23643)
          , l = t(91500);
        let u = [{
            name: "mobile",
            width: 375,
            icon: "device-mobile"
        }, {
            name: "tablet",
            width: 960,
            icon: "device-tablet"
        }, {
            name: "desktop",
            width: "100%",
            icon: "device-desktop"
        }];
        function f() {
            let {0: e, 1: r} = (0,
            n.useState)("desktop")
              , {0: t, 1: i} = (0,
            n.useState)("100%");
            return (0,
            l.jsxs)("div", {
                className: "preview",
                children: [(0,
                l.jsx)("iframe", {
                    className: "preview-iframe",
                    src: a.lX,
                    frameBorder: "0",
                    style: {
                        width: t
                    }
                }), (0,
                l.jsxs)("div", {
                    className: "preview-navbar",
                    children: [(0,
                    l.jsx)("div", {
                        className: "mr-auto",
                        children: (0,
                        l.jsx)(o(), {
                            href: "/",
                            className: "preview-navbar-link",
                            children: (0,
                            l.jsx)("span", {
                                className: "logo logo-white logo-square",
                                "aria-label": "Tabler"
                            })
                        })
                    }), (0,
                    l.jsx)("div", {
                        className: "preview-navbar-devices",
                        children: u.map(t=>(0,
                        l.jsx)("button", {
                            className: (0,
                            s.Z)("preview-navbar-link", {
                                active: t.name === e
                            }),
                            title: `Preview template on ${t.name}`,
                            onClick: ()=>{
                                r(t.name),
                                i(t.width)
                            }
                            ,
                            children: (0,
                            l.jsx)(c.Z, {
                                name: t.icon
                            })
                        }, t.name))
                    }), (0,
                    l.jsxs)("div", {
                        className: "ml-auto d-flex",
                        children: [(0,
                        l.jsxs)("a", {
                            href: a.M4,
                            className: "btn btn-primary btn-responsive-sm lemonsqueezy-button",
                            children: [(0,
                            l.jsx)(c.Z, {
                                name: "download"
                            }), (0,
                            l.jsx)("span", {
                                className: "btn-responsive-text",
                                children: "Download Tabler"
                            })]
                        }), (0,
                        l.jsx)("a", {
                            href: a.lX,
                            className: "preview-navbar-link ml-3",
                            children: (0,
                            l.jsx)(c.Z, {
                                name: "x"
                            })
                        })]
                    })]
                })]
            })
        }
    },
    73034: function(e) {
        !function() {
            var r = {
                229: function(e) {
                    var r, t, n, i = e.exports = {};
                    function o() {
                        throw Error("setTimeout has not been defined")
                    }
                    function s() {
                        throw Error("clearTimeout has not been defined")
                    }
                    function a(e) {
                        if (r === setTimeout)
                            return setTimeout(e, 0);
                        if ((r === o || !r) && setTimeout)
                            return r = setTimeout,
                            setTimeout(e, 0);
                        try {
                            return r(e, 0)
                        } catch (t) {
                            try {
                                return r.call(null, e, 0)
                            } catch (t) {
                                return r.call(this, e, 0)
                            }
                        }
                    }
                    !function() {
                        try {
                            r = "function" == typeof setTimeout ? setTimeout : o
                        } catch (e) {
                            r = o
                        }
                        try {
                            t = "function" == typeof clearTimeout ? clearTimeout : s
                        } catch (e) {
                            t = s
                        }
                    }();
                    var c = []
                      , l = !1
                      , u = -1;
                    function f() {
                        l && n && (l = !1,
                        n.length ? c = n.concat(c) : u = -1,
                        c.length && p())
                    }
                    function p() {
                        if (!l) {
                            var e = a(f);
                            l = !0;
                            for (var r = c.length; r; ) {
                                for (n = c,
                                c = []; ++u < r; )
                                    n && n[u].run();
                                u = -1,
                                r = c.length
                            }
                            n = null,
                            l = !1,
                            function(e) {
                                if (t === clearTimeout)
                                    return clearTimeout(e);
                                if ((t === s || !t) && clearTimeout)
                                    return t = clearTimeout,
                                    clearTimeout(e);
                                try {
                                    t(e)
                                } catch (r) {
                                    try {
                                        return t.call(null, e)
                                    } catch (r) {
                                        return t.call(this, e)
                                    }
                                }
                            }(e)
                        }
                    }
                    function m(e, r) {
                        this.fun = e,
                        this.array = r
                    }
                    function d() {}
                    i.nextTick = function(e) {
                        var r = Array(arguments.length - 1);
                        if (arguments.length > 1)
                            for (var t = 1; t < arguments.length; t++)
                                r[t - 1] = arguments[t];
                        c.push(new m(e,r)),
                        1 !== c.length || l || a(p)
                    }
                    ,
                    m.prototype.run = function() {
                        this.fun.apply(null, this.array)
                    }
                    ,
                    i.title = "browser",
                    i.browser = !0,
                    i.env = {},
                    i.argv = [],
                    i.version = "",
                    i.versions = {},
                    i.on = d,
                    i.addListener = d,
                    i.once = d,
                    i.off = d,
                    i.removeListener = d,
                    i.removeAllListeners = d,
                    i.emit = d,
                    i.prependListener = d,
                    i.prependOnceListener = d,
                    i.listeners = function(e) {
                        return []
                    }
                    ,
                    i.binding = function(e) {
                        throw Error("process.binding is not supported")
                    }
                    ,
                    i.cwd = function() {
                        return "/"
                    }
                    ,
                    i.chdir = function(e) {
                        throw Error("process.chdir is not supported")
                    }
                    ,
                    i.umask = function() {
                        return 0
                    }
                }
            }
              , t = {};
            function n(e) {
                var i = t[e];
                if (void 0 !== i)
                    return i.exports;
                var o = t[e] = {
                    exports: {}
                }
                  , s = !0;
                try {
                    r[e](o, o.exports, n),
                    s = !1
                } finally {
                    s && delete t[e]
                }
                return o.exports
            }
            n.ab = "//";
            var i = n(229);
            e.exports = i
        }()
    },
    33729: function(e, r, t) {
        "use strict";
        /**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
        var n = t(15387)
          , i = Symbol.for("react.element")
          , o = Symbol.for("react.fragment")
          , s = Object.prototype.hasOwnProperty
          , a = n.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner
          , c = {
            key: !0,
            ref: !0,
            __self: !0,
            __source: !0
        };
        function l(e, r, t) {
            var n, o = {}, l = null, u = null;
            for (n in void 0 !== t && (l = "" + t),
            void 0 !== r.key && (l = "" + r.key),
            void 0 !== r.ref && (u = r.ref),
            r)
                s.call(r, n) && !c.hasOwnProperty(n) && (o[n] = r[n]);
            if (e && e.defaultProps)
                for (n in r = e.defaultProps)
                    void 0 === o[n] && (o[n] = r[n]);
            return {
                $$typeof: i,
                type: e,
                key: l,
                ref: u,
                props: o,
                _owner: a.current
            }
        }
        r.Fragment = o,
        r.jsx = l,
        r.jsxs = l
    },
    91500: function(e, r, t) {
        "use strict";
        e.exports = t(33729)
    },
    51697: function(e, r, t) {
        e.exports = t(11332)
    }
}, function(e) {
    e.O(0, [332, 600, 643, 105, 592, 744], function() {
        return e(e.s = 57863)
    }),
    _N_E = e.O()
}
]);

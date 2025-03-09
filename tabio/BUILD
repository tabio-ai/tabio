load("@pip//:requirements.bzl", "requirement")
load("//tools:lint.bzl", "lint", "py_import_test")

package(default_visibility = ["//visibility:public"])

py_binary(
    name = "df_plotter",
    srcs = ["df_plotter.py"],
    deps = [
        requirement("matplotlib"),
    ],
)

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        ":df_plotter",
        requirement("absl-py"),
        requirement("pandas"),
        requirement("tk"),
    ],
)

py_import_test("main")

lint()

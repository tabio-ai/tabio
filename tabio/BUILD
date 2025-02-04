load("@pip//:requirements.bzl", "requirement")
load("//tools:lint.bzl", "lint", "py_import_test")

package(default_visibility = ["//visibility:public"])

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        requirement("pandas"),
        requirement("tk"),
    ],
)

py_import_test("main")

lint()

load("@pip//:requirements.bzl", "requirement")
load(":lint.bzl", "lint")

package(default_visibility = ["//visibility:public"])

py_binary(
    name = "buildifier",
    srcs = ["buildifier.py"],
)

exports_files([
    "flake8.sh",
])

lint()

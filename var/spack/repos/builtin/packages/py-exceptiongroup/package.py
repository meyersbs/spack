# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyExceptiongroup(PythonPackage):
    """This is a backport of the BaseExceptionGroup and ExceptionGroup classes from
    Python 3.11."""

    homepage = "https://github.com/agronholm/exceptiongroup"
    pypi     = "exceptiongroup/exceptiongroup-1.1.0.tar.gz"

    maintainers("meyersbs")

    version("1.1.0", sha256="bcb67d800a4497e1b404c2dd44fca47d3b7a5e5433dbab67f96c1a685cdfdf23")

    depends_on("py-flit-scm", type="build")
    depends_on("python@3.7:", type=("build", "run"))

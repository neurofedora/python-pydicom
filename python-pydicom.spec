%global modname pydicom
%global commit f6191c7f67d44ac942a259821bc8f436c37005be
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        1.0.0
Release:        0.3.git%{shortcommit}%{?dist}
Summary:        Read, modify and write DICOM files with python code

# There are generated data (private dict) in special format from GDCM
License:        MIT and BSD
URL:            https://github.com/darcymason/%{modname}
Source0:        https://github.com/darcymason/%{modname}/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
pydicom is a pure python package for working with DICOM files. It was made for
inspecting and modifying DICOM data in an easy "pythonic" way. The
modifications can be written again to a new file.

pydicom is not a DICOM server, and is not primarily about viewing images. It is
designed to let you manipulate data elements in DICOM files with python code.

Limitations -- the main limitation of the current version is that compressed
pixel data (e.g. JPEG) cannot be altered in an intelligent way as it can for
uncompressed pixels. Files can always be read and saved, but compressed pixel
data cannot easily be modified.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python-setuptools python-six
BuildRequires:  python-sphinx
# Test deps
BuildRequires:  numpy python-dateutil
Requires:       python-dateutil
Recommends:     numpy
Recommends:     python-matplotlib
Recommends:     tkinter
Recommends:     python-pillow

%description -n python2-%{modname}
pydicom is a pure python package for working with DICOM files. It was made for
inspecting and modifying DICOM data in an easy "pythonic" way. The
modifications can be written again to a new file.

pydicom is not a DICOM server, and is not primarily about viewing images. It is
designed to let you manipulate data elements in DICOM files with python code.

Limitations -- the main limitation of the current version is that compressed
pixel data (e.g. JPEG) cannot be altered in an intelligent way as it can for
uncompressed pixels. Files can always be read and saved, but compressed pixel
data cannot easily be modified.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools python3-six
BuildRequires:  python3-sphinx
# Test deps
BuildRequires:  python3-numpy python3-dateutil
Requires:       python3-dateutil
Recommends:     python3-numpy
Recommends:     python3-matplotlib
Recommends:     python3-tkinter
Recommends:     python3-pillow

%description -n python3-%{modname}
pydicom is a pure python package for working with DICOM files. It was made for
inspecting and modifying DICOM data in an easy "pythonic" way. The
modifications can be written again to a new file.

pydicom is not a DICOM server, and is not primarily about viewing images. It is
designed to let you manipulate data elements in DICOM files with python code.

Limitations -- the main limitation of the current version is that compressed
pixel data (e.g. JPEG) cannot be altered in an intelligent way as it can for
uncompressed pixels. Files can always be read and saved, but compressed pixel
data cannot easily be modified.

Python 3 version.

%prep
%autosetup -n %{modname}-%{commit}

# Remove shebang from one of contrib files, users still run this as pythonX /usr/lib...
# other contrib files also doesn't use shebangs
sed -i -e '1{\@^#!/usr/bin/python@d}' %{modname}/contrib/dicom_dao.py

%build
#pushd source/
 %py2_build
 %py3_build
#popd

pushd docs
  export PYTHONPATH=../
  make html SPHINXBUILD=sphinx-build BUILDDIR=_build-2
  make html SPHINXBUILD=sphinx-build-%{python3_version} BUILDDIR=_build-3
  find -name '.buildinfo' -delete
popd

%install
#pushd source/
  %py2_install
  %py3_install
#popd

%check
export LC_ALL="en_US.UTF-8"

#pushd source/
  %{__python2} setup.py test
  %{__python3} setup.py test
#popd

%files -n python2-%{modname}
%license %{modname}/license.txt
%doc README.md docs/_build-2/html
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license %{modname}/license.txt
%doc README.md docs/_build-3/html
%{python3_sitelib}/%{modname}*

%changelog
* Sun Nov 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-0.3.gitf6191c7
- Fix provide macro for py3 (typo)
- Remove shebang from dicom_dao.py (non-executable-script)

* Sun Nov 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-0.2.gitf6191c7
- Include license file
- Add BSD to license list (generated data) from GDCM

* Tue Nov 03 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-0.1.gitf6191c7
- Simplify building docs

* Sat Oct 31 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-0.0.gitf6191c7
- Initial package

%global modname pydicom
%global commit f6191c7f67d44ac942a259821bc8f436c37005be
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{modname}
Version:        1.0.0
Release:        0.0.git%{shortcommit}%{?dist}
Summary:        Read, modify and write DICOM files with python code

License:        MIT
URL:            https://github.com/darcymason/%{modname}
Source0:        https://github.com/darcymason/%{modname}/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz
Patch0:         pydicom-1.0.0-insert-path-docs.patch
BuildRequires:  git-core
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
%{?python_provide:%python_provide python2-%{modname}}
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
%autosetup -n %{modname}-%{commit} -S git

%build
#pushd source/
 %py2_build
 %py3_build
#popd

sed -i -e "/SPHINXBUILD * = sphinx-build/s/=/?=/" docs/Makefile
cp -a docs docs-3
pushd docs
  SPHINXBUILD=sphinx-build make html
popd
pushd docs-3
  SPHINXBUILD=sphinx-build-%{python3_version} make html
popd
find -name '.buildinfo' -delete

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
%doc README.md docs/_build/html
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%doc README.md docs-3/_build/html
%{python3_sitelib}/%{modname}*

%changelog
* Sat Oct 31 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-0.0.gitf6191c7
- Initial package

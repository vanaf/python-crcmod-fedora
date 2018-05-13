# Created by pyp2rpm-3.3.0
%global pypi_name crcmod

Name:           python-%{pypi_name}
Version:        1.7
Release:        1%{?dist}
Summary:        CRC Generator

License:        MIT
URL:            http://crcmod.sourceforge.net/
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
The software in this package is a Python module for generating objects that
compute the Cyclic Redundancy Check (CRC). There is no attempt in this package
to explain how the CRC works. There are a number of resources on the web that
give a good explanation of the algorithms. Just do a Google search for “crc
calculation” and browse till you find what you need. Another resource can be
found in chapter 20 of the book “Numerical Recipes in C” by Press et. al.

This package allows the use of any 8, 16, 24, 32, or 64 bit CRC. You can
generate a Python function for the selected polynomial or an instance of the
Crc class which provides the same interface as the md5 and sha modules from
the Python standard library. A Crc class instance can also generate C/C++
source code that can be used in another application.

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
The software in this package is a Python module for generating objects that
compute the Cyclic Redundancy Check (CRC). There is no attempt in this package
to explain how the CRC works. There are a number of resources on the web that
give a good explanation of the algorithms. Just do a Google search for “crc
calculation” and browse till you find what you need. Another resource can be
found in chapter 20 of the book “Numerical Recipes in C” by Press et. al.

This package allows the use of any 8, 16, 24, 32, or 64 bit CRC. You can
generate a Python function for the selected polynomial or an instance of the
Crc class which provides the same interface as the md5 and sha modules from
the Python standard library. A Crc class instance can also generate C/C++
source code that can be used in another application.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The software in this package is a Python module for generating objects that
compute the Cyclic Redundancy Check (CRC). There is no attempt in this package
to explain how the CRC works. There are a number of resources on the web that
give a good explanation of the algorithms. Just do a Google search for “crc
calculation” and browse till you find what you need. Another resource can be
found in chapter 20 of the book “Numerical Recipes in C” by Press et. al.

This package allows the use of any 8, 16, 24, 32, or 64 bit CRC. You can
generate a Python function for the selected polynomial or an instance of the
Crc class which provides the same interface as the md5 and sha modules from
the Python standard library. A Crc class instance can also generate C/C++
source code that can be used in another application.

%package -n python-%{pypi_name}-doc
Summary:        crcmod documentation
%description -n python-%{pypi_name}-doc
Documentation for crcmod

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%files -n python2-%{pypi_name}
%license LICENSE
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sun May 13 2018 Ivan Afonichev <ivan.afonichev@gmail.com> - 1.7-1
- Initial package.

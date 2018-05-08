Name: python-crcmod
Summary: CRC Generator
Version: 1.7
Release: 1%{?dist}
Group: Development/Libraries
License: MIT
URL: http://crcmod.sourceforge.net/
Source0: http://pypi.python.org/packages/source/c/crcmod/crcmod-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python-devel
BuildRequires: python-setuptools

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

%prep
%setup -q -n crcmod-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%{python_sitearch}/*

%changelog
* Tue Apr 07 2015 Vladimir Rusinov <vladimir@greenmice.info> - 1.7-1
- initial version

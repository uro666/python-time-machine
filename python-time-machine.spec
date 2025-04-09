%define module time-machine
%define oname time_machine
# disable test for abf
%bcond_with test

Name:		python-time-machine
Version:	2.16.0
Release:	1
Summary:	Travel through time in your tests
URL:		https://github.com/adamchainz/time-machine
License:	MIT
Group:		Development/Python
Source0:	https://github.com/adamchainz/time-machine/archive/refs/tags/%{version}/%{module}-%{version}.tar.gz
BuildSystem:	python

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(python-dateutil)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	timezone
%if %{with test}
BuildRequires:	python%{pyver}dist(iniconfig)
BuildRequires:	python%{pyver}dist(coverage)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pluggy)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-randomly)
BuildRequires:	python%{pyver}dist(python-dateutil)
BuildRequires:	python%{pyver}dist(six)
%endif
Requires:	python%{pyver}dist(python-dateutil)
Requires:	timezone

%description
Travel through time in your tests.

%prep
%autosetup -n %{module}-%{version} -p1

%build
%py3_build

%install
%py3_install

%if %{with test}
%check
pip install -e .[test]
pytest -v tests/
%endif

%files
%{python3_sitearch}/%{oname}
%{python3_sitearch}/%{oname}-%{version}.dist-info
%{python3_sitearch}/_%{oname}.*.so
%license LICENSE
%doc README.rst

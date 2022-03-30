#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module		tabulate
Summary:	Pretty-print tabular data
Name:		python-%{module}
Version:	0.8.9
Release:	5
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/tabulate/
Source0:	https://files.pythonhosted.org/packages/source/t/tabulate/%{module}-%{version}.tar.gz
# Source0-md5:	71e6f214512ceda2892be47767156754
URL:		https://github.com/astanin/python-tabulate
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pretty-print tabular data in Python.

The main use cases of the library are:
- printing small tables without hassle: just one function call,
  formatting is guided by the data itself
- authoring tabular data for lightweight plain-text markup: multiple
  output formats suitable for further editing or transformation
- readable presentation of mixed textual and numeric data: smart
  column alignment, configurable number formatting, alignment by a
  decimal point

%package -n python3-%{module}
Summary:	Pretty-print tabular data
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
Pretty-print tabular data in Python.

The main use cases of the library are:
- printing small tables without hassle: just one function call,
  formatting is guided by the data itself
- authoring tabular data for lightweight plain-text markup: multiple
  output formats suitable for further editing or transformation
- readable presentation of mixed textual and numeric data: smart
  column alignment, configurable number formatting, alignment by a
  decimal point

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG README.md
%if %{without python3}
%attr(755,root,root) %{_bindir}/tabulate
%endif
%{py_sitescriptdir}/%{module}.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG README.md
%attr(755,root,root) %{_bindir}/tabulate
%{py3_sitescriptdir}/__pycache__/%{module}.cpython-*.py[co]
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

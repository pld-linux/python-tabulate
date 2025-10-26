#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_with	python3	# CPython 3.x module (built from python3-tabulate.spec)

%define		module		tabulate
Summary:	Pretty-print tabular data
Summary(pl.UTF-8):	Ładne wypisywanie danych tabelarycznych
Name:		python-%{module}
# keep 0.8.x here for python2 support
Version:	0.8.10
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/tabulate/
Source0:	https://files.pythonhosted.org/packages/source/t/tabulate/%{module}-%{version}.tar.gz
# Source0-md5:	70cc6906675fc840e2675ecd022641bc
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

%description -l pl.UTF-8
Ładne wypisywanie danych tabelarycznych w Pythonie.

Główne przypadki użycia tej biblioteki to:
- proste wypisywanie małych tabelek - tylko jedno wywołanie funkcji,
  formatowanie sugerowane przez same dane
- tworzenie danych tabelarycznych do lekkich znaczników tekstowych -
  wiele formatów wyjściowych, odpowiednich do dalszej edycji lub
  przekształceń
- czytelna prezentacja mieszanych danych tekstowych i liczbowych -
  inteligentne wyrównywanie kolumn, konfigurowalne formatowanie liczb,
  wyrównywanie do kropki/przecinka dziesiętnego

%package -n python3-%{module}
Summary:	Pretty-print tabular data
Summary(pl.UTF-8):	Ładne wypisywanie danych tabelarycznych
Group:		Libraries/Python
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

%description -n python3-%{module} -l pl.UTF-8
Ładne wypisywanie danych tabelarycznych w Pythonie.

Główne przypadki użycia tej biblioteki to:
- proste wypisywanie małych tabelek - tylko jedno wywołanie funkcji,
  formatowanie sugerowane przez same dane
- tworzenie danych tabelarycznych do lekkich znaczników tekstowych -
  wiele formatów wyjściowych, odpowiednich do dalszej edycji lub
  przekształceń
- czytelna prezentacja mieszanych danych tekstowych i liczbowych -
  inteligentne wyrównywanie kolumn, konfigurowalne formatowanie liczb,
  wyrównywanie do kropki/przecinka dziesiętnego

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

%{__mv} $RPM_BUILD_ROOT%{_bindir}/tabulate{,-2}
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
%attr(755,root,root) %{_bindir}/tabulate-2
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

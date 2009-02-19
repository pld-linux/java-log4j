# TODO:
# - rename to apache-log4j?
# - some tests fail, but it seems to be an error in tests, not in log4j
#
# NOTE:
# - javamail is provided by java-gnu-mail
# - jmx,jndi by java-sun-jre
#
# Conditional build:
%bcond_without	dist	# build components which can't be distributed
%bcond_with	jms	# JMS interface (org.apache.log4j.or.jms)
%bcond_with	jmx	# JMX interface (org.apache.log4j.jmx)
%bcond_with	tests	# tun tests
#
%if %{without dist}
%define	with_jms	1
%define	with_jmx	1
%endif
#
%include	/usr/lib/rpm/macros.java
Summary:	log4j - logging for Java
Summary(pl.UTF-8):	log4j - zapis logów dla Javy
Name:		logging-log4j
Version:	1.2.15
Release:	4
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/logging/log4j/%{version}/apache-log4j-%{version}.tar.gz
# Source0-md5:	10f04abe4d68d5a89e8eb167e4e45e1a
URL:		http://logging.apache.org/log4j/
Patch0:		apache-log4j-javadoc.patch
Patch1:		%{name}-sourcetarget.patch
BuildRequires:	ant >= 1.7.1-4
%{?with_tests:BuildRequires:	ant-junit}
BuildRequires:	java-activation
BuildRequires:	java-gcj-compat
BuildRequires:	javamail >= 1.2
BuildRequires:	jaxp_parser_impl
%{?with_jms:BuildRequires:	jms >= 1.1}
%{?with_jmx:BuildRequires:	jmx-tools >= 1.2.1}
%{?with_jmx:BuildRequires:	jmx >= 1.2.1}
%{?with_jmx:BuildRequires:	jndi}
BuildRequires:	jpackage-utils
%{?with_tests:BuildRequires:	junit >= 3.8}
BuildRequires:	rpmbuild(macros) >= 1.300
Suggests:	java-mail >= 1.2
%{?with_jms:Suggests:	jms >= 1.1}
%{?with_jmx:Suggests:	jmx-tools >= 1.2.1}
Provides:	log4j = %{version}
Obsoletes:	jakarta-log4j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With log4j it is possible to enable logging at runtime without
modifying the application binary.

%description -l pl.UTF-8
Przy użyciu log4j można włączyć zapis do logów przy uruchamianiu bez
modyfikowania binarnej aplikacji.

%package doc
Summary:	Online manual for log4j
Summary(pl.UTF-8):	Dokumentacja online do log4j
Group:		Documentation
Obsoletes:	jakarta-log4j-doc

%description doc
Online manual for log4j.

%description doc -l pl.UTF-8
Dokumentacja online do log4j.

%package javadoc
Summary:	API documentation for log4j
Summary(pl.UTF-8):	Dokumentacja API log4j
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-log4j-doc

%description javadoc
API documentation for log4j.

%description javadoc -l pl.UTF-8
Dokumentacja API log4j.

%prep
%setup -q -n apache-log4j-%{version}
%patch0 -p1
%patch1 -p1

%build
required_jars="mail activation %{?with_jms:jms} %{?with_jmx:jmx jmxtools}"
CLASSPATH=$(build-classpath $required_jars); export CLASSPATH
%ant -Dbuild.compiler=gcj -Dbuild.rmic=forking jar javadoc

%if %{with tests}
cd tests
CLASSPATH=$(build-classpath junit)
export CLASSPATH
%ant -Dbuild.compiler=gcj build runAll
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{name}-%{version}}
cp -a dist/lib/log4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/log4j-%{version}.jar
ln -s log4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/log4j.jar

cp -a docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc LICENSE NOTICE
%{_javadir}/log4j-%{version}.jar
%{_javadir}/log4j.jar

%files doc
%defattr(644,root,root,755)
%doc site/{css,images,xref,xref-test,*.html}

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

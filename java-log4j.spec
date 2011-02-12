# TODO:
# - some tests fail, but it seems to be an error in tests, not in log4j
#
# NOTE:
# - jmx,jndi by java-sun-jre
#
# Conditional build:
%bcond_without	dist		# build components which can't be distributed
%bcond_with	java_sun	# build with java-sun
%bcond_with	jms		# JMS interface (org.apache.log4j.or.jms)
%bcond_with	jmx		# JMX interface (org.apache.log4j.jmx)
%bcond_with	tests		# tun tests
#
%if %{without dist}
%define	with_jms	1
%define	with_jmx	1
%endif

%define		srcname	log4j
#
%include	/usr/lib/rpm/macros.java
Summary:	log4j - logging for Java
Summary(pl.UTF-8):	log4j - zapis logów dla Javy
Name:		java-%{srcname}
Version:	1.2.16
Release:	1
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/logging/log4j/%{version}/apache-%{srcname}-%{version}.tar.gz
# Source0-md5:	8e331a930d0b56280a1c66a00621b3a3
Patch0:		apache-log4j-javadoc.patch
Patch1:		logging-%{srcname}-sourcetarget.patch
Patch2:		%{name}-version.patch
URL:		http://logging.apache.org/log4j/
BuildRequires:	ant >= 1.7.1-4
%{?with_tests:BuildRequires:	ant-junit}
BuildRequires:	java(javamail) >= 1.2
BuildRequires:	java(jaxp_parser_impl)
%{?with_jmx:BuildRequires:	java(jmx) >= 1.2.1}
BuildRequires:	jdk
%{?with_jms:BuildRequires:	jms >= 1.1}
%{?with_jmx:BuildRequires:	jmx-tools >= 1.2.1}
%{?with_jmx:BuildRequires:	java(jndi)}
BuildRequires:	jpackage-utils
%{?with_tests:BuildRequires:	junit >= 3.8}
BuildRequires:	rpmbuild(macros) >= 1.300
Suggests:	java(javamail) >= 1.2
%{?with_jms:Suggests:	jms >= 1.1}
%{?with_jmx:Suggests:	jmx-tools >= 1.2.1}
Provides:	log4j = %{version}
Obsoletes:	jakarta-log4j
Obsoletes:	log4j
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
Obsoletes:	logging-log4j-doc

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
Obsoletes:	logging-log4j-javadoc

%description javadoc
API documentation for log4j.

%description javadoc -l pl.UTF-8
Dokumentacja API log4j.

%prep
%setup -q -n apache-log4j-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__rm} log4j-%{version}.jar

%build
required_jars="mail activation %{?with_jms:jms} %{?with_jmx:jmx jmxtools}"
CLASSPATH=$(build-classpath $required_jars); export CLASSPATH
%ant jar javadoc

%if %{with tests}
cd tests
CLASSPATH=$(build-classpath $required_jars junit)
export CLASSPATH
%ant build runAll
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir}/%{srcname}-%{version}}
cp -a dist/lib/%{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

cp -a docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

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
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}

#
# TODO:
# - do something with jms / jmx requirements;
#   http://lists.pld-linux.org/mailman/pipermail/pld-devel-en/2006-May/017648.html
#
# NOTE:
# - javamail is provided by java-gnu-mail
# - jmx by java-sun-jre
#
%include	/usr/lib/rpm/macros.java
Summary:	log4j - logging for Java
Summary(pl):	log4j - zapis logów dla Javy
Name:		jakarta-log4j
Version:	1.2.13
Release:	1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/logging/log4j/%{version}/logging-log4j-%{version}.tar.gz
# Source0-md5:	080a645669672dd3fc22f0d8deaf06ac
URL:		http://logging.apache.org/log4j/
BuildRequires:	ant
BuildRequires:	javamail >= 1.2
BuildRequires:	jdk >= 1.2
#BuildRequires:	jms
BuildRequires:	jpackage-utils
BuildRequires:	junit >= 3.8
BuildRequires:	jmx
Requires:	javamail >= 1.2
Requires:	jdk >= 1.2
#Requires:	jms
Requires:	junit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With log4j it is possible to enable logging at runtime without
modifying the application binary.

%description -l pl
Przy u¿yciu log4j mo¿na w³±czyæ zapis do logów przy uruchamianiu bez
modyfikowania binarnej aplikacji.

%package doc
Summary:	Online manual for log4j
Summary(pl):	Dokumentacja online do log4j
Group:		Development/Languages/Java

%description doc
Online manual for log4j.

%description doc -l pl
Dokumentacja online do log4j.

%prep
%setup -q -n logging-log4j-%{version}

%build
unset JAVA_HOME || :
export JAVA_HOME="%{java_home}"

# is this required?  doesn't ant do it?
required_jars="javamail jms activation junit jmxri jmxtools"
export CLASSPATH="`/usr/bin/build-classpath $required_jars`"

ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install dist/lib/log4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -sf log4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/log4j.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs/*

Summary:	log4j - logging for Java
Summary(pl):	log4j - zapis logów dla Javy
Name:		jakarta-log4j
Version:	1.1.3
Release:	3
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/builds/%{name}/release/v%{version}/%{name}-%{version}.tar.gz
Patch0:		%{name}-junit3.8.patch
URL:		http://jakarta.apache.org/
BuildRequires:	jakarta-ant
BuildRequires:	javamail >= 1.2
BuildRequires:	jdk >= 1.2
BuildRequires:	jms
BuildRequires:	junit >= 3.8
BuildRequires:	xerces-j
Requires:	javamail >= 1.2
Requires:	jdk >= 1.2
Requires:	jms
Requires:	junit
Requires:	xerces-j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

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
%setup -q
%patch -p1

%build
JAVA_HOME="/usr/lib/java"
CLASSPATH="$CLASSPATH:$JAVA_HOME/jre/lib/rt.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/mail.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/jms.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/activation.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/junit.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/classes/xerces.jar"
export JAVA_HOME CLASSPATH

sh build.sh jar
sh build.sh javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}
install dist/lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.APL
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs/*

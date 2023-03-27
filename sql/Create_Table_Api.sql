
CREATE TABLE `LOGRESTAPI` (
		`IdApi` int(5) NOT NULL AUTO_INCREMENT,
		`Url` varchar(500) default NULL,
		`Page_` varchar(500) default NULL,
		`Headers` varchar(500) default null,
		`BaseUrl` varchar(500) default null,
		`Html` longtext default null,
		`Game` varchar(200) default null,
        PRIMARY KEY(`IdApi`)
	);
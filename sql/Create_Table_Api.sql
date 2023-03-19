
CREATE TABLE `API_LOG` (
	`IdApi` mediumint(100) unsigned NOT NULL,
    `Url` varchar(100) default NULL,
    `Page` varchar(80) default NULL,
    `Headers` varchar(80) default null,
    `BaseUrl` varchar(10) default null,
    `ApiJson` JSON default null,
    `Game` varchar(80) default null,
    PRIMARY KEY (`IdApi`)
)AUTO_INCREMENT=1;
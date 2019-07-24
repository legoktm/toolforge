4.3.0 (unreleased)
------------------
* Add type hints (Lucas Werkmeister)
* Raise ValueError in toolforge.dbname() if it's not found
* Make it easy to connect to tools.db.svc.eqiad.wmflabs (Bryan Davis)

4.2.0
-----
* Turn redirect_to_https into a no-op
* Have set_user_agent return the new value
* Drop Python 3.3 support

4.1.0
-----
* Add \*.{analytics,web}.db.svc.eqiad.wmflabs support (Bryan Davis)


4.0.0
-----
* Rename library to "toolforge"

3.2.0
-----
* Add redirect_to_https() helper for flask apps

3.1.0
-----
* Add a convenience function for monkey-patching requests' user-agent

3.0.0
-----
* Initial tagged release
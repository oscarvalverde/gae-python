"""
Using redirect route instead of simple routes since it supports strict_slash
Simple route: http://webapp-improved.appspot.com/guide/routing.html#simple-routes
RedirectRoute: http://webapp-improved.appspot.com/api/webapp2_extras/routes.html#webapp2_extras.routes.RedirectRoute
"""
from webapp2_extras.routes import RedirectRoute
from bp_content.themes.mytheme.handlers import handlers

secure_scheme = 'https'

# Here go your routes, you can overwrite boilerplate routes (bp_includes/routes)

_routes = [
    RedirectRoute('/secure/', handlers.SecureRequestHandler, name='secure', strict_slash=True),
    RedirectRoute('/settings/delete_account', handlers.DeleteAccountHandler, name='delete-account', strict_slash=True),
    RedirectRoute('/contact/', handlers.ContactHandler, name='contact', strict_slash=True),
    RedirectRoute('/about/', handlers.AboutHandler, name='about', strict_slash=True),
    RedirectRoute('/privacy/', handlers.PrivacyHandler, name='privacy', strict_slash=True),  
    RedirectRoute('/terms/', handlers.TermsHandler, name='terms', strict_slash=True),  
    RedirectRoute('/advertising/', handlers.AdvertisingHandler, name='advertising', strict_slash=True),  
    RedirectRoute('/send_sms/', handlers.SendSMSHandler, name='send_sms', strict_slash=True),  
    RedirectRoute('/twiml/', handlers.TwimlHandler, name='twiml', strict_slash=True),  
]

def get_routes():
    return _routes

def add_routes(app):
    if app.debug:
        secure_scheme = 'http'
    for r in _routes:
        app.router.add(r)

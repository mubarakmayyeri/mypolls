

class SampleMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response
    
  def __call__(self, request):
    print('Middleware called before view')
    
    response = self.get_response(request)
    
    print('Middleware called after view')
    
    return response
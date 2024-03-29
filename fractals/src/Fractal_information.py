class fractal_Information:
    def __init__(self):
        self.infoVar=self.fractals()
    def fractals(self):
        fractalInfo={
            'mandelbrot': {
            'type': 'mandelbrot',
            'centerX': -0.6,
            'centerY': 0.0,
            'axisLen': 2.5,
            },

        'mandelbrot-zoomed': {
            'type': 'mandelbrot',
            'centerX': -1.0,
            'centerY': 0.0,
            'axisLen': 1.0,
            },

        'spiral0': {
            'type': 'mandelbrot',
            'centerX': -0.761335372924805,
            'centerY': 0.0835704803466797,
            'axisLen': 0.004978179931102462,
            },

        'spiral1': {
            'type': 'mandelbrot',
            'centerX': -0.747,
            'centerY': 0.1075,
            'axisLen': 0.002,
            },

        'seahorse': {
            'type': 'mandelbrot',
            'centerX': -0.745,
            'centerY': 0.105,
            'axisLen': 0.01,
            },

        'spiral1': {
            'type': 'mandelbrot',
            'centerX': -0.747,
            'centerY': 0.1075,
            'axisLen': 0.002,
            },

        'elephants': {
            'type': 'mandelbrot',
            'centerX':  0.30820836067024604,
            'centerY':  0.030620936230004017,
            'axisLen':  0.03,
            },

        'leaf': {
            'type': 'mandelbrot',
            'centerX': -1.543577002,
            'centerY': -0.000058690069,
            'axisLen':  0.000051248888,
            },

        'starfish': {
            'type': 'mandelbrot',
            'centerX': -0.463595023481762,
            'centerY': 0.598380871135558,
            'axisLen': 0.00128413675654471,
            },
        # The full julia set
            'fulljulia': {
                'type': 'julia',
                'centerX':     0.0,
                'centerY':     0.0,
                'axisLen':  4.0,
                },

        # This one looks like an hourglass
            'hourglass': {
            'type': 'julia',
            'centerX':     0.618,
            'centerY':     0.00,
            'axisLen':  0.017148277367054,
            },

        # This fractal reminds me of lakes
        'lakes': {
            'type': 'julia',
            'centerX': -0.339230468501458,
            'centerY': 0.417970758224314,
            'axisLen': 0.164938488846612,
            },

        # There are some lace curtains that look JUST LIKE THIS!
        'lace-curtains': {
            'type': 'julia',
            'centerX': -1.01537721564149,
            'centerY': 0.249425427273733,
            'axisLen': 0.0121221433855615,
            },
        }
        return fractalInfo

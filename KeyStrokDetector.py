import keyboard
import time
import random

import threading
key_count = 0
bpm = 100
interval = 60.0 / bpm
beat = 0
beat_count = 0

class Stopwatch:
    def __init__(self):
         self._elapsed_ns = 0.0
         self._t0_ns = None

    def start(self):
         if self._t0_ns is None:
              self._t0_ns = time.perf_counter_ns()
            

    def stop(self):
         if self._t0_ns is not None:
              self._elapsed_ns += time.perf_counter_ns() - self._t0_ns
              self._t0_ns = None
    
    def reset(self):
         self._elapsed_ns = 0.0
         self._t0_ns = time.perf_counter_ns()
    
    def elapsed(self):
        acc = self._elapsed_ns
        if self._t0_ns is not None:
             acc += time.perf_counter_ns() - self._t0_ns
             return acc / 1_000_000_000.0
        
        
        #return self._elapsed + (time.perf_counter() - self._t0 if self._running else 0.0)
    


sw = Stopwatch()







def every(second, func):
    t = threading.Timer(second, lambda: (func(), every(second, func)))
    t.daemon = True
    t.start()
    return t



def tick():
    global MaxCount
    MaxCount = random.randint(200, 400)
    

every(.01, tick)


def on_up(e):
     print(sw.elapsed())
     sw.stop()
     sw.reset()
        
    



def on_press(e):
    global key_count, beat_count
    #print(f"down: {e.name}")
    sw.start()
    key_count += 1
    if key_count >= MaxCount:
        print("Way To fast")
    if sw.elapsed() < 0.05:
        print("kick")
    if sw.elasped() < 0.60:
        beat_count += 1
    if beat_count == 10:
        print("kick")
        
         

    print(key_count)
    on_up(e)
    
    
    
    
    
    


keyboard.on_press(on_press)
keyboard.on_release(on_up)
keyboard.wait("esc") 
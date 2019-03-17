import threading
import queue
import sys


class FileSound(object):
    buffersize = 20
    blocksize = 2048
    q = queue.Queue(maxsize=buffersize)
    event = threading.Event()

    def play_sound(self):
        # sd.play(self.data, self.fs, device=sd.default.device)

        def callback_out(outdata, frames, time, status):
            assert frames == self.blocksize
            if status.output_underflow:
                print('Output underflow: increase blocksize?', file=sys.stderr)
                raise sd.CallbackAbort
            assert not status
            try:
                data = self.q.get_nowait()
            except queue.Empty:
                print('Buffer is empty: increase buffersize?', file=sys.stderr)
                raise sd.CallbackAbort
            if len(data) < len(outdata):
                outdata[:len(data)] = data
                outdata[len(data):] = b'\x00' * (len(outdata) - len(data))
                raise sd.CallbackStop
            else:
                outdata[:] = data
        try:
            import soundfile as sf
            import sounddevice as sd
            import numpy
            assert numpy

            with sf.SoundFile("C:/Users/turch/Desktop/Al.wav") as self.f:
                for _ in range(self.buffersize):
                    data = self.f.buffer_read(self.blocksize, dtype='float32')
                    if not data:
                        break
                    self.q.put_nowait(data)  # Pre-fill queue

                stream = sd.RawOutputStrsteam(device=sd.default.device,
                                         samplerate=self.f.samplerate,
                                         blocksize=self.blocksize,
                                         dtype='float32',
                                         channels=self.f.channels,
                                         callback=callback_out,
                                         finished_callback=self.event.set)
                print(self.f.channels)
                with stream:
                    timeout = self.blocksize * self.buffersize / self.f.samplerate
                    while data:
                        data = self.f.buffer_read(self.blocksize, dtype='float32')
                        self.q.put(data, timeout=timeout)
                    self.event.wait()
        except sd.PortAudioError:
            print("Error opening file sound")
        except Exception as e:
            print(type(e).__name__ + ': ' + str(e))

    def pause_sound(self):
        pass

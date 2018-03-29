import unittest
from timeadd import add_times, parse_times, TimeStruct
from timeuntil import time_until

class TestStruct(unittest.TestCase):
    
    def test_simple(self):
        zero = TimeStruct(0,0)
        ones = TimeStruct(1,1)
        onetwothree = TimeStruct(1,23)

        self.assertEqual(zero.minutes, 0)
        self.assertEqual(zero.hours, 0)

        self.assertEqual(ones.minutes,1)
        self.assertEqual(ones.hours, 1)

        self.assertEqual(onetwothree.minutes, 23)
        self.assertEqual(onetwothree.hours, 1)


class TestParser(unittest.TestCase):

    def test_zeros(self):
        zero = TimeStruct(0,0)
        time1 = parse_times("0:0", "0")
        time2 = parse_times("0:00", "0:00")
        time3 = parse_times("0", "00")
        self.assertEqual(time1, time2)
        self.assertEqual(time1, time3)
        self.assertEqual(time1, time3)
        self.assertEqual(time1, (zero, zero))


    def test_time_storage(self):
        time1 = parse_times("1:00", "23")[0]
        self.assertEqual(time1.hours, 1)
        self.assertEqual(time1.minutes, 0)

        time2 = parse_times("4:23", "76")[0]
        self.assertEqual(time2.hours, 4)
        self.assertEqual(time2.minutes, 23)

        time3 = parse_times("2", "6")[0]
        self.assertEqual(time3.hours, 2)
        self.assertEqual(time3.minutes, 0)

        time4 = parse_times("6:", "12")[0]
        self.assertEqual(time4.hours, 6)
        self.assertEqual(time4.minutes, 0)
        
    def test_delta_storage(self):
        delta1 = parse_times("0", "3")[1]
        self.assertEqual(delta1.minutes, 3)
        self.assertEqual(delta1.hours, 0)

        delta2 = parse_times("2:42", "62")[1]
        self.assertEqual(delta2.hours, 0)
        self.assertEqual(delta2.minutes, 62)

        delta3 = parse_times("1", "1:41")[1]
        self.assertEqual(delta3.hours, 1)
        self.assertEqual(delta3.minutes, 41)

        delta4 = parse_times("32", "4:")[1]
        self.assertEqual(delta4.hours, 4)
        self.assertEqual(delta4.minutes, 0)

        delta5 = parse_times("3:33", ":12")[1]
        self.assertEqual(delta5.hours, 0)
        self.assertEqual(delta5.minutes, 12)

    def test_now(self):
        parse_times("now", "12")
        pass


class TestAdd(unittest.TestCase):
    
    def setUp(self):
        self.ts = [TimeStruct(i, 0) for i in range(0, 13)]

    def test_self(self):
        self.assertEqual(0, self.ts[0].hours)
        self.assertEqual(12, self.ts[-1].hours)
        self.assertEqual(13, len(self.ts))

    def test_zero(self):
        zero = TimeStruct(0, 0)
        self.assertEqual(zero, add_times(zero, zero))

    def test_hours(self):
        ts = self.ts

        self.assertEqual(ts[3], add_times(ts[1], ts[2]))
        self.assertEqual(ts[5], add_times(ts[3], ts[2]))
        self.assertEqual(ts[12], add_times(ts[7], ts[5]))

    def test_rollover_hours(self):
        ts = self.ts

        self.assertEqual(ts[1], add_times(ts[12], ts[1]))
        self.assertEqual(ts[2], add_times(ts[12], ts[2]))
        self.assertEqual(ts[12], add_times(ts[8], ts[4]))
        self.assertEqual(ts[1], add_times(ts[8], ts[5]))
        self.assertEqual(ts[12], add_times(ts[12], ts[12]))

        self.assertEqual(ts[12], add_times(ts[12], TimeStruct(36, 0)))


    def test_rollover_mins(self):
        t1 = add_times(TimeStruct(10, 30), TimeStruct(0, 30))
        self.assertEqual(t1, TimeStruct(11, 0))

        t2 = add_times(TimeStruct(10, 31), TimeStruct(0, 30))
        self.assertEqual(t2, TimeStruct(11, 1))

        t3 = add_times(TimeStruct(10, 30), TimeStruct(0, 29))
        self.assertEqual(t3, TimeStruct(10, 59))


    def test_rollover_both(self):
        t1 = add_times(TimeStruct(12, 30), TimeStruct(0, 30))
        self.assertEqual(t1, TimeStruct(1, 0))

        t2 = add_times(TimeStruct(12, 32), TimeStruct(1, 30))
        self.assertEqual(t2, TimeStruct(2, 2))


class TestUntil(unittest.TestCase):
    twelve = TimeStruct(12, 0)

    def test_zero(self):
        t1 = time_until(self.twelve, now=self.twelve)
        self.assertEqual(t1, TimeStruct(0, 0))

    def test_hours(self):
        t1 = time_until(TimeStruct(1, 0), now=self.twelve)
        self.assertEqual(t1, TimeStruct(1, 0))

    def test_minutes(self):
        t1 = time_until(TimeStruct(12, 54), now=self.twelve)
        self.assertEqual(t1, TimeStruct(0, 54))

    def test_rollover_minutes(self):
        t1 = time_until(TimeStruct(2, 30), now=TimeStruct(12, 40))
        self.assertEqual(t1, TimeStruct(1, 50))
        t2 = time_until(TimeStruct(2, 1), now=TimeStruct(1, 58))
        self.assertEqual(t2, TimeStruct(0, 3))


if __name__ == "__main__":
    unittest.main()


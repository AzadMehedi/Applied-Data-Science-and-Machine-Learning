# A list of coordinate pairs and a helper to compute centroids.

coords = [(0,0), (2,2), (4,0), (2,-2)]

def centroid(points):
    if not points:
        return None
    xs = [p[0] for p in points]  # coord এর x অক্ষের জন্য ভ্যালু গুলো নিবে মানে প্রতিটা টাপলের 1st ইন্ডেক্স এর ভ্যালু নিয়ে লিস্ট বানাবে।
    ys = [p[1] for p in points]  # coord এর y অক্ষের জন্য ভ্যালু গুলো নিবে মানে প্রতিটা টাপলের 2nd ইন্ডেক্স এর ভ্যালু নিয়ে লিস্ট বানাবে।লু।
    return (sum(xs)/len(xs), sum(ys)/len(ys))  # এখানে অক্ষদ্বয়ের কেন্দ্রবিন্দু বের করা হয়েছে।
    

if __name__ == '__main__':
    print('Coordinates: ', coords)
    print('Centroid: ', centroid(coords))


# Centroid মানে হলো সব পয়েন্টের গড় অবস্থান।
# এই উদাহরণে (2, 0) হলো সেই কেন্দ্রবিন্দু — এটি আসলে চারটি বিন্দুর মাঝে ঠিক মাঝখানে পড়ে (একটা ডায়মন্ড আকৃতির মাঝখানে)।


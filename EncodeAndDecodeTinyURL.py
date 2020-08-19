class Codec:
    STRING = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hashMap = {}
    count=1
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        tag = self.genTag()
        self.hashMap[tag] = longUrl
        return "http://tinyurl.com/" + tag
        self.count+=1
    
    def genTag(self):
        
        c=self.count
        sb=""
        while c>0:
            c-=1
            sb+=self.STRING[c%62]
            c/=62
        return sb    
        

    
    
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        idx = shortUrl.split('/')[-1]
        if idx in self.hashMap:
            return self.hashMap[idx]
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

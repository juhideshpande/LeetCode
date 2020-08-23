r = len(maze)
		c = len(maze[0])
		path = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		stack = [(start[0], start[1])]        
		seen = {(start[0], start[1])}
		while stack:
			x, y = stack.pop()
			for a, b in path:
				nx = x
				ny = y
				while 0 <= nx < r and 0 <= ny < c and maze[nx][ny] == 0:
					nx += a
					ny += b
				nx -= a
				ny -= b
				if [nx, ny] == destination:
					return True
				else:
					if (nx, ny) not in seen:
						stack.append((nx, ny))
						seen.add((nx, ny))

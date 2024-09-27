from collections import deque

def count_nodes(graph, start, n):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1  # 시작 노드도 포함하여 카운트 시작

    print(f"\nBFS 시작 - 시작 노드: {start}")

    while queue:
        node = queue.popleft()
        print(f"현재 노드: {node}, 큐 상태: {list(queue)}")

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
                print(f"방문 노드: {neighbor}, 큐에 추가됨. 현재 방문한 노드 수: {count}")

    print(f"BFS 종료 - 총 방문한 노드 수: {count}\n")
    return count

def solution(n, wires):
    # 그래프 생성 (리스트로)
    graph = [[] for _ in range(n + 1)]  # 노드 번호가 1부터 시작하므로 n+1개 생성
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    min_difference = n  # 가능한 최대 차이로 초기화

    # 모든 연결을 하나씩 제거해보면서 최소 차이 계산
    for a, b in wires:
        # 연결 제거
        graph[a].remove(b)
        graph[b].remove(a)

        # 송전탑 개수 계산
        count_a = count_nodes(graph, a, n)
        count_b = n - count_a  # 전체에서 한쪽 개수를 빼면 나머지 개수

        # 최소 차이 갱신
        min_difference = min(min_difference, abs(count_a - count_b))

        # 제거한 연결 복구
        graph[a].append(b)
        graph[b].append(a)

    return min_difference

# 예시 실행
n = 9
wires = [[1,3], [2,3], [3,4], [4,5], [4,6], [4,7], [7,8], [7,9]]
print("최소 차이:", solution(n, wires))

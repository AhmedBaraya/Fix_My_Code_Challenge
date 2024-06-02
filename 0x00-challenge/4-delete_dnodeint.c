int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    // ... existing code to find the node at the index ...

    if (node == NULL) {
        return -1; // Handle invalid index or empty list
    }

    // Update previous and next pointers of surrounding nodes
    if (node->prev) {
        node->prev->next = node->next;
    } else {
        // Update head if deleting the head node
        *head = node->next;
    }
    if (node->next) {
        node->next->prev = node->prev;
    }

    // Free the memory allocated for the deleted node
    free(node);

    return 1;
}

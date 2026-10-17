import { Button } from "./Button";

export function ApprovalActions({
  isWaiting,
  onAnswer,
}: {
  isWaiting: boolean;
  onAnswer: (isApproved: boolean) => void;
}) {
  return (
    <span className="approval-actions">
      <Button isDisabled={!isWaiting} onClick={() => onAnswer(false)}>
        Turn down
      </Button>
      <Button isPrimary isDisabled={!isWaiting} onClick={() => onAnswer(true)}>
        Approve plan
      </Button>
    </span>
  );
}
